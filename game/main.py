from terminal import terminal
import sys
import select
import tty
from sprites import Sprite
from map import Map
import copy
import glob
import time

@terminal.wrapper
def main(term):
    tree = Sprite(20, 5, "tree", "templates/tree_8x5.txt")
    hero = Sprite(3, 3, "hero", "templates/hero_10x9.txt")
    map1 = Map("lvl1_map_basic", 80, 24, term)
    map1.add_terrain(tree)
    map1.add_hero(hero)

    items = []

    # start game
    term.clear()
    term.write_template(0, 0, "templates/80x24_blank.txt")
    term.write_template(10, 10, "templates/want_ad.txt")
    str = term.block_read(1)
    term.clear()
    term.move(0,0)

    mx, my = hero.x, hero.y
    while True:
        term.poll_input()
        chr = term.read_char() 

        if chr == 'q':
            break

        if chr == terminal.KEY_LEFT:
            if not test_collide(hero, 1, 0, items):
                if mx < (80 - hero.width):
                    mx += 1

        if chr == terminal.KEY_RIGHT:
            if not test_collide(hero, -1, 0, items):
                if mx > 1:
                    mx -= 1

            if chr == terminal.KEY_DOWN:
                if not test_collide(hero, 0, -1, items):
                    if my > 1:
                        my -= 1

            if chr == terminal.KEY_UP:
                if not test_collide(hero, 0, 1, items):
                    if my < (24 - hero.height):
                        my += 1
        mx = abs(mx)
        my = abs(my)
        term.write("MX: %d, MY: %d\r\n" % (mx, my))

    # exit the game
    term.cleanup()
