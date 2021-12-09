import sys
from math import prod

file = open(sys.argv[1]).readlines()

data = [[int(i) for i in row.strip()] for row in file]

rows = len(data)
cols = len(data[0])

low_points = []

for row_index in range(0, rows):
    for col_index in range(0, cols):

        position = data[row_index][col_index]

        # Up
        if row_index == 0:
            up = 10
        else:
            up = data[row_index - 1][col_index]

        # Down
        if row_index == rows - 1:
            down = 10
        else:
            down = data[row_index + 1][col_index]

        # Left
        if col_index == 0:
            left = 10
        else:
            left = data[row_index][col_index - 1]

        # Right
        if col_index == cols - 1:
            right = 10
        else:
            right = data[row_index][col_index + 1]

        if position < right and position < left and position < down and position < up:
            low_points.append(position)

print("Low points: {}".format(low_points))
print("Overall risk: {}".format(sum([i + 1 for i in low_points])))


def get_basin_id(index: int):
    while grid[index] != index:
        grid[index] = index = grid[grid[index]]
    return index


def connect_basins(a, b):
    grid[get_basin_id(a)] = get_basin_id(b)


grid = list(range(rows * cols))

for y in range(rows):
    for x in range(cols):
        index = y * cols + x
        if data[y][x] != 9:
            if y > 0 and data[y - 1][x] != 9:
                connect_basins(index, index - cols)
            if x + 1 < cols and data[y][x + 1] != 9:
                connect_basins(index, index + 1)
            if y + 1 < rows and data[y + 1][x] != 9:
                connect_basins(index, index + cols)
            if x > 0 and data[y][x - 1] < 9:
                connect_basins(index, index - 1)

basinsizes = [0] * len(grid)
for b in grid:
    basinsizes[get_basin_id(b)] += 1
total_size = prod(sorted(basinsizes, reverse=True)[:3])

print(f"Part 2: {total_size}")
