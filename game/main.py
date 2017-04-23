from terminal import terminal
import sys
import select
import tty
import sprite
import copy
import glob
import time

def wait_input(total):
    while True:
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            str = sys.stdin.read(total)
            if len(str) == total:
                return str

@terminal.wrapper
def main(term):
    tree = sprite.sprite(5, 5, "tree", "templates/tree_8x5.txt")
    hero = sprite.sprite(3, 3, "hero", "templates/hero_10x9.txt")
    items = []

    # start game
    term.clear()
    term.write_template(0, 0, "templates/80x24_blank.txt")
    term.write_template(10, 10, "templates/want_ad.txt")
    str = wait_input(1)
    term.clear()
    hero.draw(term, 3, 3)
    tree.draw(term, 40, 2)
    term.move(0,0)

    mx, my = hero.x, hero.y
    while True:
        chr = wait_input(1)
        if chr == 'q':
            break
        if chr == '\x1b':
            chr = wait_input(2)
            if chr == '[C':
                if not test_collide(hero, 1, 0, items):
                    if mx < (80 - hero.width):
                        mx += 1
            if chr == '[D':
                if not test_collide(hero, -1, 0, items):
                    if mx > 1:
                        mx -= 1
            if chr == '[A':
                if not test_collide(hero, 0, -1, items):
                    if my > 1:
                        my -= 1
            if chr == '[B':
                if not test_collide(hero, 0, 1, items):
                    if my < (24 - hero.height):
                        my += 1
        mx = abs(mx)
        my = abs(my)
        #term.write("\33[42m")
        hero.draw(term, mx, my)
    term.cleanup()

