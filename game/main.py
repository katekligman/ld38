from terminal import terminal
import sys
import select
import tty
from sprites import Terrain, Hero, Portal, Slime, Spider, Ghost, Skeleton, Eyeball
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

    term.clear()

    # Load first story 
    term.write_template(0, 5, "assets/ansi/story_backdrop_80x24.ansi")
    term.write_template(25, 6, "templates/story1.txt")
    term.block_read(1) # press almost any char to continue 

    l = Level(1, term)
    l.load_level()
    l.start_level()

    # start game
    term.move(0,0)

    while True:
        term.poll_input()
        chr = term.read_char() 

        if chr == 'q':
            break

        if chr == terminal.KEY_LEFT:
            l.hero = l.hero.move(-1, 0)

        if chr == terminal.KEY_RIGHT:
            l.hero = l.hero.move(1, 0)

        if chr == terminal.KEY_DOWN:
            l.hero = l.hero.move(0, 1)

        if chr == terminal.KEY_UP:
            l.hero = l.hero.move(0, -1)

    # exit the game
    term.cleanup()
