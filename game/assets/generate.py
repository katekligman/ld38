#!/usr/bin/env python3

import subprocess
import glob

for k in glob.glob("*.png"):
    #resize = "resize/" + k + "_resize.png"
    #subprocess.call(["/usr/local/bin/convert", "-fuzz", "1%", "-resize", images[k], "-trim", k + ".png", resize])
    p = subprocess.Popen(["/usr/local/bin/identify", k], stdout=subprocess.PIPE)
    line = str(p.stdout.readline())
    geometry = line.split(' ')[2]
    subprocess.call(["/usr/local/bin/img2xterm", k, "ansi/" + k + "_" + geometry + ".ansi"])
