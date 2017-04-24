import configparser
from map import Map
from sprites import *

class Level(object):

    def __init__(self, level_num, term):
        self.level_num = int(level_num)
        self.maps = []
        self.term = term
        self.hero = Hero(5, 15, "hero")

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

    def start_level(self):
        self.maps[0].render()

    def load_level(self):

        # Add maps and portals
        next_portal = None
        for i in range(0, self.level_num + 1):
            map = Map('level_' + str(self.level_num) + '_map_' + str(i+1), 80, 24, self.term)

            # Note: The first and last maps only have one portal
            if next_portal is not None:
                map.add_sprite(next_portal)
            # Otherwise two portals per map
            if i < self.level_num:
                portal = Portal(30, 12, "portal" + str(i+1))
                next_portal = Portal(20, 5, "portal" + str(i+1))
                portal.add_to_portal(next_portal)
                next_portal.add_to_portal(portal)
                map.add_sprite(portal)
            else:
                next_portal = None
            self.maps.append(map)
    
        self.maps[0].add_sprite(self.hero)

        for map in self.maps:
            for i in self.max_monsters:
                while True:
                    x = random.randint(5, 65)
                    y = random.randint(3, 19)
                    try:
                        monster_class_name = random.choice(self.monsters)
                        module = __import__('sprites')
                        dyn_class = getattr(module, monster_class_name)
                        s = dyn_class(x, y, monster_class_name + str(i))
                        #s.set_home_map(random.choice(self.maps).name)
                        s.set_home_map(map.name)
                        map.add_sprite(s)
                        break
                    except:
                        print(sys.exc_info()[0])
                        continue


