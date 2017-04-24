import re
import terminal
import sys
import handlers
import random

class MoveMixin(object):

    def move(self, x_delta, y_delta):

        # NOTE this is only implemented for hero
        new_self = self.__class__(
            x=self.x + x_delta,
            y=self.y + y_delta,
            name=self.name,
            path=self.path
        )

        # Temporarily remove map from self since it's in limbo
        map = self.map

        self.map.pop_sprite(self.name)

        if map.is_valid(new_self):
            collision_sprite = map.is_collision(new_self)
            if not collision_sprite:
                map.undraw(self)
                map.add_sprite(new_self)
                map.draw(new_self)
                return new_self
            else:
                self.collision_handler.trigger(self, collision_sprite, map)
                return self
        else:
            # Add map back to self because it still exists in map
            map.add_sprite(self)
            return self


class Sprite(object):

    classtype = "sprite"
    collision_type = "blocking"

    def __init__(self, x, y, name, path):
        self.x = x
        self.y = y
        self.name = name
        self.path = path
        self.map = None
        self.collision_handler = handlers.collision_handler
        self.teleportation_handler = handlers.teleportation_handler

        p = re.compile('.*?(\d+)x(\d+).txt')
        m = p.match(path)
        if m:
            self.width = int(m.group(1))
            self.height = int(m.group(2))
        else:
            raise

    def add_map(self, map):

        if self.map is not None:
            raise Exception("sprite already has map")

        self.map = map

    def remove_map(self):

        self.map = None

    def check_collision(self, sprite):
        # NOTE this is not commutative.
        # Only run with objects already in map
        if self.map is None:
            return False

        hero_left = self.x
        hero_right = self.x + self.width
        hero_top = self.y
        hero_bottom = self.y + self.height

        sprite_left = sprite.x
        sprite_right = sprite.x + sprite.width
        sprite_top = sprite.y
        sprite_bottom = sprite.y + sprite.height

        if not (
            ((hero_right < sprite_left) or (hero_left > sprite_right)) or
            ((hero_bottom < sprite_top) or (hero_top > sprite_bottom))
        ):
            return True
        return False

class Portal(Sprite):

    classtype = "portal"
    collision_type = "portal"

    def __init__(self, *args, **kwargs):
        self.to_portal = None
        super(Portal, self).__init__(*args, **kwargs)

    def add_to_portal(self, portal):
        self.to_portal = portal

class Creature(Sprite, MoveMixin):

    classtype = "creature"
    collision_type = "creature"

    def __init__(self, *args, **kwargs):

        super(Creature, self).__init__(*args, **kwargs)

        self.home_map = None

    def set_home_map(self, name):
        self.home_map = name

class Slime(Creature):
    # Doesnt move
    pass

class Spider(Creature):

    def act(self):
        go_right = bool(random.getrandbits(1))
        go_down = bool(random.getrandbits(1))

        x_delta = 1 if go_right else -1
        y_delta = 1 if go_down else -1

        self.move(x_delta, y_delta)

class Ghost(Creature):

    def act(self):
        horizontal = bool(random.getrandbits(1))
        movement = random.randint(-2, 2)
        if horizontal:
            self.move(movement, 0)
        else:
            self.move(0, movement)

class Skeleton(Creature):

    def act(self):
        self.move(random.randint(-1, 1), random.randint(-1, 1))

class Eyeball(Creature):

    def act(self):
        self.move(random.randint(-2, 2), 0)

class Terrain(Sprite):

    classtype = "terrain"
    collision_type = "blocking"

class Hero(Sprite, MoveMixin):

    classtype = "hero"
    collision_type = "hero"

    def __init__(self, *args, **kwargs):

        super(Hero, self).__init__(*args, **kwargs)

        self.backpack = dict()

    def free_creatures(self):
        """frees creatures from backpack"""

        if self.map.name not in self.backpack:
            return

        for creature in self.backpack[self.map.name]:
            self.map.add_sprite(creature)
            self.map.draw(creature)

    def grab(self, creature):
        # Assume the creature has already been removed from map
        if creature.home_map in self.backpack:
            self.backpack[creature.home_map].append(creature)
        else:
            self.backpack[creature.home_map] = [creature]
