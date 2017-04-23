import re
import terminal
import sys

class Sprite(object):

    classtype = "sprite"

    def __init__(self, x, y, name, path):
        self.x = x
        self.y = y
        self.name = name
        self.path = path
        self.map = None

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

class Creature(Sprite):

    classtype = "creature"

class Terrain(Sprite):

    classtype = "terrain"

class Hero(Sprite):

    classtype = "hero"

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
            map.undraw(self)
            map.add_sprite(new_self)
            map.draw(new_self)
            return new_self
        else:
            # Add map back to self because it still exists in map
            map.add_sprite(self)
            return self

