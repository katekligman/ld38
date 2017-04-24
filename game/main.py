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

@terminal.wrapper
def main(term):

    # title screen
    term.write_template(0, 5, "templates/title.txt")
    term.block_read(1) # press almost any char to continue
    term.flush()

    term.clear()

    lvl = 1
    while True:
        term.flush()
        l = Level(lvl, term)
        if l.start_level() == False:
            break
        lvl += 1

    # exit the game
    term.cleanup()

    # maybe show some stats?
