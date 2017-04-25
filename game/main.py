from terminal import terminal
import sys
import select
import tty
from sprites import Terrain, Hero, Portal, Slime, Scorpion, Ghost, Skeleton, Eyeball
from map import Map
import copy
import glob
import time
import random
from levels import Level
import time

@terminal.wrapper
def main(term):

    try:
        # title screen
        term.write_template(0, 5, "templates/title.txt")
        time.sleep(1)
        term.block_read(1)
        term.flush()
        term.clear()

        # want ad
        term.write_template(0, 5, "assets/ansi/story_backdrop_80x24.ansi")
        term.write_template(20, 7, "templates/want_ad.txt")
        time.sleep(1)
        term.block_read(1)
        term.flush()

        # instructions
        term.write_template(0, 5, "assets/ansi/story_backdrop_80x24.ansi")
        term.write_template(16, 7, "templates/instructions1.txt")
        time.sleep(1)
        term.block_read(1)
        term.flush()

        term.clear()

        lvl = 1
        while True:
            term.flush()
            l = Level(lvl, term)
            if l.start_level() == False:
                break
            lvl += 1
            time.sleep(100/1000.0)

        # exit the game
        term.cleanup()
    except:
        print(sys.exc_info()[1])
        sys.exit(0)
    # maybe show some stats?
    sys.exit(0)
