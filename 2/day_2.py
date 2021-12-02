from os import X_OK
import sys


x = 0
y = 0
a = 0

for i in open(sys.argv[1]).readlines():

    key, val = i.strip().split()
    val = int(val)

    if key == "forward":
        y += a * val
        x += val
    if key == "up":
        # y -= val
        a -= val
    if key == "down":
        a += val
        # y += val

print("x: {}, y: {}, Position: {}".format(x, y, x * y))
