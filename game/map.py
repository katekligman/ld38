class Map(object):

    def __init__(self, name, width, height, term):

        self.term = term
        self.name = name
        self.width = width
        self.height = height
        self.sprite = dict()

    def draw(self, sprite):
        self.term.write_template(sprite.x, sprite.y, sprite.path)

    def render(self):
        """
        This draws everything over again
        """

        self.term.clear()

        self.draw(self.hero)

        for s in self.sprites.values():
            self.draw(s)

    def add_sprite(self, sprite):

        if self.is_valid(sprite):
            self.sprites[sprite.name] = sprite
        else:
            raise Exception("Cant add")

        sprite.add_map(self)

    def remove(self, name):

        sprite = self.sprites.pop(name)

        for y1 in range(sprite.y, sprite.y + sprite.height):
            self.term.move(sprite.x, y1)
            self.term.write(' ' * sprite.width)

    def is_valid(self, sprite):

        # Check there isn't a name collision
        if sprite.name in self.sprites:
            return False

        # Checks if there's collision
        for t in self.terrains:
            if t.check_collision(sprite):
                return False

        for c in self.creatures:
            if c.check_collision(sprite):
                return False

        if self.hero and self.hero.check_collision(sprite):
            return False

        if not self.in_map(sprite):
            return False

        return True

    def in_map(self, sprite):

        if (0 <= sprite.x  and sprite.x <= self.width) and (0  <= sprite.y and sprite.y <= self.height):
            return True

        return False
