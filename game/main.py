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

    hero = Hero(3, 15, "hero", "assets/ansi/hero_5x5.ansi")

    # Level 1 - Slime World

    portal = Portal(30, 12, "portal", "templates/terrain/portal_8x8.txt")
    portal2 = Portal(20, 5, "portal2", "templates/terrain/portal_8x8.txt")
    portal.add_to_portal(portal2)
    portal2.add_to_portal(portal)

    map1 = Map("lvl1_map1_basic", 80, 24, term)
    map2 = Map("lvl1_map2_basic", 80, 24, term)
    map1.add_sprite(hero)
    map1.add_sprite(portal)
    map2.add_sprite(portal2)

    for i in range(3):
        while True:
            x = random.randint(5, 65)
            y = random.randint(3, 19)
            try:
                s = Slime(x, y, "slime" + str(i), "assets/ansi/slime_7x5.ansi")
                map1.add_sprite(s)
                break
            except:
                continue

    # start game
    map1.render()
    term.move(0,0)

    while True:
        map1.act()
        term.poll_input()
        chr = term.read_char() 

        if chr == 'q':
            break

        if chr == terminal.KEY_LEFT:
            hero = hero.move(-1, 0)

        if chr == terminal.KEY_RIGHT:
            hero = hero.move(1, 0)

        if chr == terminal.KEY_DOWN:
            hero = hero.move(0, 1)

        if chr == terminal.KEY_UP:
            hero = hero.move(0, -1)

    # exit the game
    term.cleanup()
