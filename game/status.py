from sprites import Creature
from sprites import Sprite

class Status(Sprite):

    def __init__(self, x, y, width, height, term, title, name, hero):

        self.map = None
        self.term = term
        self.hero = hero
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.title = title
        self.name = name

    def draw(self):
        """
        This draws everything over again
        """

        self.map.undraw(self)

        current_y = self.y
        # Render map name
        self.term.move(self.x, current_y)
        self.term.write(self.title)

        # Render creature counts
        current_y += 3
        message = ["Boss : Get those", "buggers back", "to their home", "dimensions"]
        self.term.move(self.x, current_y)
        for line in message:
            self.term.write(line)
            current_y += 1
            self.term.move(self.x, current_y)

        current_y += 3
        self.term.move(self.x, current_y)
        self.term.write("Your backpack:")
        for key in self.hero.backpack:
            for creature in self.hero.backpack[key]:
                current_y += 1
                self.term.move(self.x, current_y)
                self.term.write("    -" + creature.name)
