import curses
import culour

begin_x = 20; begin_y = 7
height = 10; width = 40

curses.initscr()
curses.start_color()
win = curses.newwin(height, width, begin_y, begin_x)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK);
win.attron(curses.color_pair(1));
#culour.addstr(win, "\033 1;1hi")
start = "\033[1;31m"
end = "\033[0;0m"
culour.addstr(win,  "File is: " + start + "<placeholder>" + end)
