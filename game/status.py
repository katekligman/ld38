from sprites import Creature
from sprites import Sprite

class Status(Sprite):

    def __init__(self, x, y, width, height, term, name, hero):

        self.map = None
        self.term = term
        self.hero = hero
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def draw(self):
        """
        This draws everything over again
        """

        current_y = self.y
        # Render map name
        self.term.move(self.x, current_y)
        self.term.write(self.map.name.upper())

        # Render creature counts
        current_y += 3
        self.term.move(self.x, current_y)
        self.term.write("Creatures:")
        current_y += 1
        for creature in self.map.sprites.values():
            if isinstance(creature, Creature):
                self.term.move(self.x, current_y)
                self.term.write("    -" + creature.name)
                current_y += 1

        current_y += 1

        self.term.move(self.x, current_y)
        self.term.write("Your backpack:")
        for key in self.hero.backpack:
            for creature in self.hero.backpack[key]:
                current_y += 1
                self.term.move(self.x, current_y)
                self.term.write("    -" + creature.name)
