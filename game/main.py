from terminal import terminal
import sys
import select
import tty
from sprites import Terrain, Hero, Creature, Portal
from map import Map
import copy
import glob
import time

@terminal.wrapper
def main(term):
    tree = Terrain(20, 5, "tree", "templates/terrain/tree_8x5.txt")
    hero = Hero(3, 3, "hero", "templates/creatures/hero_10x9.txt")
    map1 = Map("lvl1_map_basic", 80, 24, term)
    map1.add_sprite(tree)
    map1.add_sprite(hero)

    items = []

    # start game
    term.clear()
    term.write_template(0, 0, "templates/80x24_blank.txt")
    term.write_template(10, 10, "templates/want_ad.txt")
    str = term.block_read(1)
    map1.render()
    term.move(0,0)

    mx, my = hero.x, hero.y
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
