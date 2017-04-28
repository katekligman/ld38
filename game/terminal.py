import sys
import tty
import termios
import subprocess
import select
import time

class terminal(object):
    KEY_RIGHT = "\x1b[C" 
    KEY_LEFT = "\x1b[D" 
    KEY_UP = "\x1b[A" 
    KEY_DOWN = "\x1b[B" 
    KEYS = [KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN]

    ANSI_CURSOR_HIDE = "\033[?25l"
    ANSI_CURSOR_SHOW = "\033[?25h"


    def __init__(self):
        self.input_buffer = ""

    def cleanup(self):
        pass
        #subprocess.call("reset")

    @staticmethod
    def wrapper(main):
        # keep the original terminal attributes for cleanup
        terminfo_orig = termios.tcgetattr(sys.stdin)
        # new terminal settings 
        settings_new = termios.tcgetattr(sys.stdin)
        settings_new[3] = settings_new[3] & ~(termios.ECHO | termios.ICANON)
        settings_new[6][termios.VMIN] = 0
        settings_new[6][termios.VTIME] = 0
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings_new)
        #tty.setcbreak(sys.stdin.fileno())
        term = terminal().clear()
        term.write(term.ANSI_CURSOR_HIDE)
        try:
            main(term)
        except:            
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminfo_orig)
            term.write(term.ANSI_CURSOR_SHOW)
            subprocess.call("reset")
            raise

    def clear(self):
        sys.stdout.write("\33[2J")
        return self

    def move(self, x, y):             
        sys.stdout.write("\33[%d;%dH" % (y, x))

    def write(self, str):
        sys.stdout.write(str)

    def has_input(self):
        return len(self.input_buffer)

    def block_read(self, total):
        self.input_buffer = sys.stdin.read(total)

    def _read_input_buffer(self):
        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            time.sleep(1/1000.0)
            s = sys.stdin.read(3)
            if s:
                self.input_buffer += str(s)
            else:
                sys.exit(0)

    def poll_input(self):
        self._read_input_buffer()
    
    def read_char(self):
        # Nothing available
        if len(self.input_buffer) == 0:
            return ""

        # arrow keys
        for key in terminal.KEYS:
            if self.input_buffer[0:3] == key:
                self.input_buffer = self.input_buffer[len(key):]
                return key

        char = self.input_buffer[0]
        if char != '\x33' and char != '[':
            self.input_buffer = self.input_buffer[1:]
            return char

        return ''

    def _flush_input_buffer(self):
        self.input_buffer = []
        sys.stdin.flush()
    
    def flush(self):
        self._flush_input_buffer()

    def write_template(self, x, y, path, vars = {}):
       with open(path, 'r') as f:
        i = y
        self.move(x, y)
        for line in f:
            self.move(x, i)
            try:
                self.write(line % vars)
            except:
                self.write(line)
            i += 1
