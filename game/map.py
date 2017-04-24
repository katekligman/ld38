import time
import random
import sprites

ACT_INTERVAL = .25

class Map(object):

    def __init__(self, name, width, height, term, number):

        self.term = term
        self.name = name
        self.pretty_name = "Dimension: " + str(number)
        self.number = number
        self.width = width
        self.height = height
        self.sprites = dict()
        self.active_sprites = dict()
        self.last_acted_at = 0

    def draw(self, sprite):
        if hasattr(sprite, 'draw'):
            sprite.draw()
        else:
            # to fix
            note = "X"
            #if hasattr(sprite, 'home_map'):
            #    note = sprite.home_map.number
            self.term.write_template(sprite.x, sprite.y, sprite.path, note)

    def act(self):
        current_time = time.time()
        if (time.time() - self.last_acted_at) > ACT_INTERVAL:
            for sprite in self.active_sprites.values():
                sprite.act()
            self.last_acted_at = current_time

    def render(self):
        """
        This draws everything over again
        """

        self.term.clear()

        for s in self.sprites.values():
            self.draw(s)

        self.last_acted_at = time.time()

    def add_sprite(self, sprite):

        if not self.is_valid(sprite):
            raise Exception("Not valid!!")

        while True:
            if not self.is_collision(sprite):
                self.sprites[sprite.name] = sprite
                break
            else:
                # Hack to get sprite onto map. Random coordinates
                sprite.x = random.randint(0, self.width - sprite.width)
                sprite.y = random.randint(0, self.height - sprite.height)
                continue

        if hasattr(sprite, "act"):
            self.active_sprites[sprite.name] = sprite

        sprite.add_map(self)

    def pop_sprite(self, name):
        sprite = self.sprites.pop(name)
        sprite.remove_map()

        if name in self.active_sprites:
            self.active_sprites.pop(name)

        return sprite

    def undraw(self, sprite):

        self.undraw_coordinates(
            sprite.x,
            sprite.y,
            sprite.width,
            sprite.height
        )

    def undraw_coordinates(self, x, y, width, height):
        for y1 in range(y, y + height):
            self.term.move(x, y1)
            self.term.write(' ' * width)

    def is_collision(self, sprite):
        # Checks if there's collision
        for s in self.sprites.values():
            if s.check_collision(sprite):
                return s

        return False

    def is_valid(self, sprite):

        # Check there isn't a name collision
        if sprite.name in self.sprites:
            return False

        if not self.in_map(sprite):
            return False

        return True

    def in_map(self, sprite):

        if (0 <= sprite.x  and sprite.x + sprite.width <= self.width) and (0  <= sprite.y and sprite.y + sprite.height <= self.height):
            return True

        return False
