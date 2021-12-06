from collections import Counter
import sys


def graph(vents, diagonal):
    cells = []

    for x0, y0, x1, y1 in vents:

        x0 = int(x0)
        y0 = int(y0)
        x1 = int(x1)
        y1 = int(y1)

        dx = 0 if x0 == x1 else 1 if x0 < x1 else -1
        dy = 0 if y0 == y1 else 1 if y0 < y1 else -1

        sz = 1 + max(abs(x0 - x1), abs(y0 - y1))

        if diagonal or dx == 0 or dy == 0:

            cells.extend([(x0 + i * dx, y0 + i * dy) for i in range(sz)])

    count = Counter(cells)

    return sum(1 for c in count if count[c] > 1)


inputs = [
    i.strip().replace(" -> ", ",").split(",") for i in open(sys.argv[1]).readlines()
]

print(graph(inputs, diagonal=True))
