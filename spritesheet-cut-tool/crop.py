from sys import argv
from PIL import Image

_, old_image, new_image, x1, y1, x2, y2 = argv

img = Image.open(old_image)
img2 = img.crop((int(x1), int(y1), int(x2), int(y2)))
img2.save(new_image)
