class Map(object):

    def __init__(self, name, width, height, term):

        self.term = term
        self.name = name
        self.width = width
        self.height = height
        self.terrains = []
        self.creatures = []
        self.hero = None
        self.portals = []

    def draw(self, sprite):
        self.term.write_template(sprite.x, sprite.y, sprite.path)

    def add_terrain(self, terrain):

        if self.is_valid(terrain):
            self.terrains.append(terrain)
        else:
            raise Exception("Cant add")

        self.terrain.add_map(self)
        self.draw(terrain)

    def add_creature(self, creature):

        if self.is_valid(creature):
            self.creatures.append(creature)
        else:
            raise Exception("Cant add")

        self.creature.add_map(self)
        self.draw(creature)

    def add_portal(self, portal):
        if self.is_valid(portal):
            self.portals.append(portal)
        else:
            raise Exception("Cant add")

        self.portal.add_map(self)
        self.draw(portal)

    def add_hero(self, hero):

        if self.is_valid(hero):
            self.hero = hero
        else:
            raise Exception("Cant add")

        self.hero.add_map(self)
        self.draw(hero)

    def remove_hero(self):

        for y1 in range(self.hero.y, self.hero.y + self.hero.height):
            self.term.move(self.hero.x, y1)
            self.term.write(' ' * self.hero.width)

        self.hero = None

    def is_valid(self, sprite):

        # Checks if there's collision
        for t in self.terrains:
            if sprite.check_collision(t):
                return False

        for c in self.creatures:
            if sprite.check_collision(c):
                return False

        if self.hero and sprite.check_collision(self.hero):
            return False

        if not self.in_map(sprite):
            return False

        return True

    def in_map(self, sprite):

        if (0 <= sprite.x  and sprite.x <= self.width) and (0  <= sprite.y and sprite.y <= self.height):
            return True

        return False
