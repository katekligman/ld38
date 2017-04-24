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
    tree = Terrain(20, 5, "tree", "templates/terrain/tree_8x5.txt")
    hero = Hero(3, 20, "hero", "templates/creatures/hero_10x9.txt")
    eyeball = Creature(50, 5, "eyeball", "templates/creatures/eyeball_11x11.txt")
    #birdman = Creature(30, 5, "birdman", "templates/creatures/birdman_10x16.txt")
    portal = Portal(30, 5, "portal", "templates/terrain/portal_8x8.txt")
    map1 = Map("lvl1_map_basic", 80, 24, term)
    map1.add_sprite(tree)
    map1.add_sprite(eyeball)
    map1.add_sprite(hero)
    #map1.add_sprite(birdman)
    map1.add_sprite(portal)

    items = []

    # start game
    term.clear()
    term.write_template(0, 0, "templates/80x24_blank.txt")
    term.write_template(10, 10, "templates/want_ad.txt")
    str = term.block_read(1)
    map1.render()
    term.move(0,0)

    mx, my = hero.x, hero.y
    last_moved_time = int(time.time() * 1000)
    while True:
        current_time = int(time.time() * 1000)
        if (current_time - last_moved_time) > 250:
            eyeball = eyeball.move(random.randint(-1, 1), random.randint(-1, 1))
            #birdman = birdman.move(random.randint(-1, 1), random.randint(-1, 1))
            last_moved_time = int(time.time() * 1000)

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
