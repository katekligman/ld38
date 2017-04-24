from terminal import terminal
import sys
import select
import tty
from sprites import Terrain, Hero, Creature, Portal
from map import Map
import copy
import glob
import time
import random

@terminal.wrapper
def main(term):
    #tree = Terrain(20, 5, "tree", "templates/terrain/tree_8x5.txt")
    hero = Hero(3, 20, "hero", "templates/creatures/hero_10x9.txt")
    #eyeball = Creature(50, 5, "eyeball", "templates/creatures/eyeball_11x11.txt")
    #birdman = Creature(30, 5, "birdman", "templates/creatures/birdman_10x16.txt")
    portal = Portal(30, 12, "portal", "templates/terrain/portal_8x8.txt")
    portal2 = Portal(20, 5, "portal2", "templates/terrain/portal_8x8.txt")
    portal.add_to_portal(portal2)
    portal2.add_to_portal(portal)
    map1 = Map("lvl1_map_basic", 80, 24, term)
    #map1.add_sprite(tree)
    #map1.add_sprite(eyeball)
    map1.add_sprite(hero)
    #map1.add_sprite(birdman)
    map1.add_sprite(portal)

    map2 = Map("lvl1_map2_basic", 80, 24, term)
    map2.add_sprite(portal2)

    items = []

    # start game
    term.clear()
    term.write_template(0, 0, "templates/80x24_blank.txt")
    term.write_template(10, 10, "templates/want_ad.txt")
    str = term.block_read(1)
    map1.render()
    term.move(0,0)

    while True:

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
