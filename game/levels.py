from terminal import terminal
import configparser
from map import Map
from sprites import *
from status import Status
import time

class Level(object):

    def __init__(self, level_num, term):
        self.level_num = int(level_num)
        self.maps = []
        self.term = term
        self.hero = Hero(5, 15, "hero")
        self.hero.level = self
        self.status = None
        self.is_won = False

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

        self.load_level()

    def start_level(self):

        # Show the intro story
        self.term.write_template(0, 5, "assets/ansi/story_backdrop_80x24.ansi")
        self.term.write_template(25, 6, self.intro_template)
        self.term.block_read(1) 

        self.maps[0].render()

        # begin level
        self.term.move(0,0)
        while True:
            self.term.poll_input()
            chr = self.term.read_char() 

            if chr == 'q':
                self.term.clear()
                return False

            if chr == self.term.KEY_LEFT:
                self.hero = self.hero.move(-1, 0)

            if chr == self.term.KEY_RIGHT:
                self.hero = self.hero.move(1, 0)

            if chr == self.term.KEY_DOWN:
                self.hero = self.hero.move(0, 1)

            if chr == self.term.KEY_UP:
                self.hero = self.hero.move(0, -1)

            if self.is_won:
                self.term.flush()
                self.term.clear()

                # Show the summary
                self.term.write_template(0, 5, "assets/ansi/story_backdrop_80x24.ansi")
                self.term.write_template(25, 6, self.summary_template)
                time.sleep(3)
                self.term.block_read(1) 
                return True

    def load_level(self):

        # Add maps and portals
        next_portal = None
        for i in range(0, self.level_num + 1):
            map = Map('level_' + str(self.level_num) + '_map_' + str(i+1), 80, 24, self.term, i+1)

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
            map.add_sprite(Status(55, 1, 20, 23, self.term, 
                        "Dimension: " + str(i+1), "status", self.hero))
            self.maps.append(map)

        self.maps[0].add_sprite(self.hero)

        for j, m in enumerate(self.maps):
            for i in self.max_monsters:
                while True:
                    x = random.randint(5, 65)
                    y = random.randint(3, 19)
                    try:
                        monster_class_name = random.choice(self.monsters)
                        module = __import__('sprites')
                        dyn_class = getattr(module, monster_class_name)

                        home = random.choice(self.maps)
                        while home.name == m.name:
                            index = random.randint(0,len(self.maps)-1)
                            home = self.maps[index]
                        s = dyn_class(x, y, monster_class_name + '-' + str(index + 1) +  '.' + str(j) + '-' + str(i))
                        s.set_home_map(home)
                        m.add_sprite(s)
                        break
                    except:
                        print(sys.exc_info()[1])
                        continue


