import configparser
from map import Map
from sprites import *

class Level(object):

    def __init__(self, level_num, term):
        self.level_num = int(level_num)
        self.maps = []

        # Load levels.ini from the main game folder
        self.config = configparser.ConfigParser()
        self.config.read('levels.ini')
        self.name = 'Level ' + str(level_num)

        # Get the right section name if level is scripted or in 'Level N' endless mode
        n = 'N' if level_num > 5 else str(level_num)

        self.monsters = self.config['Level ' + n]['monsters'].split(', ')
        self.max_monsters = self.config['Level ' + n]['max_monsters']
        self.intro_template = self.config['Level ' + n]['intro']
        self.summary_template = self.config['Level ' + n]['summary']

    def load_level(self):

        next_portal = None
        for i in range(0, self.level_num + 1):
            map = Map('level_' + str(self.level_num) + '_map_' + str(i+1), 80, 24, term)

            # Note: The first and last levels only have one portal
            if next_portal is not None:
                map.add_sprite(next_portal)
            # Otherwise two portals per level
            if i < self.level_num:
                portal = Portal(30, 12, "portal" + str(i+1), "templates/terrain/portal_8x8.txt")
                next_portal = Portal(20, 5, "portal" + str(i+1), "templates/terrain/portal_8x8.txt")
                portal.add_to_portal(next_portal)
                next_portal.add_to_portal(portal)
                map.add_sprite(portal)
            else:
                next_portal = None
            self.maps.append(map)

