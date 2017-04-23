import sys

class terminal(object):

    @staticmethod
    def wrapper(main):
        term = terminal().clear()
        try:
            main(term)
        except:
            term.clear()
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

@terminal.wrapper
def main(term):
    term.write_template(0, 0, "/tmp/out.chr")
