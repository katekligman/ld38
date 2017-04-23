import sys
import tty
import termios
import subprocess

class terminal(object):
    def __init__(self):
        self.terminfo_orig = termios.tcgetattr(sys.stdin)

    def cleanup(self, term=None):
        if term == None:
	        term = self
        termios.tcsetattr(sys.stdin, termios.TCSANOW, term.terminfo_orig)
       # term.clear()
        #subprocess.call("reset")

    @staticmethod
    def wrapper(main):
        tty.setcbreak(sys.stdin.fileno())
        term = terminal().clear()
        try:
            main(term)
        except:            
            terminal.cleanup(term)
            raise

    def clear(self):
        sys.stdout.write("\33[2J")
        return self

    def move(self, x, y):             
        sys.stdout.write("\33[%d;%dH" % (y, x))

    def write(self, str):
        sys.stdout.write(str)

    def write_template(self, x, y, path, vars = {}):
       with open(path, 'r') as f:
        i = y
        self.move(x, y)
        for line in f:
            self.move(x, i)
            self.write(line % vars)
            i += 1

