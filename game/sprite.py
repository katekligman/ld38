import re
import terminal
import sys

class sprite(object):
    def __init__(self, x, y, name, path):
        self.x = x
        self.y = y
        self.name = name
        self.path = path
        p = re.compile('.*?(\d+)x(\d+).txt')
        m = p.match(path)
        if m:
            self.width = int(m.group(1))
            self.height = int(m.group(2))
        else:
            raise

    def check_collision(self, sprite):
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


    def debug(self, term):
        term.move(70, 1)
        term.write("X: " + str(self.x))
        term.move(70, 2)
        term.write("Y: " + str(self.y))
        term.move(70, 3)
        term.write("W: " + str(self.width))
        term.move(70, 4)
        term.write("H: " + str(self.height))

    def draw(self, term, x, y):
        for y1 in range(self.y, self.y+self.height):
            term.move(self.x, y1)
            term.write(' ' * self.width)

        self.x = x
        self.y = y
        term.write_template(self.x, self.y, self.path)
