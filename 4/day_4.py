import sys
import numpy as np

# Readin
with open(sys.argv[1]) as file:

    numbers = [int(i) for i in file.readline().strip().split(",")]
    file.readline()

    grids = dict()
    c = 0
    grid = []
    for line in file:
        line = line.strip()

        if line == "":
            grids["grid_" + str(c)] = grid
            grid = []
            c += 1
            continue

        row = [int(i.replace(" ", "")) for i in line.split()]
        grid.append(row)

grids["grid_" + str(c)] = grid


# Check for a winner
def check_grids(g):

    winning_grids = {}
    for grid_name, grid in g.items():

        winning_count = 0
        # Rows
        for row in grid:
            if all(ele == "nan" for ele in row):
                winning_count += 1

        for col_index in range(0, len(grid[0])):
            col = [row[col_index] for row in grid]
            if all(ele == "nan" for ele in col):
                winning_count += 1

        if winning_count > 0:
            winning_grids[grid_name] = [i[:] for i in grid]

    return winning_grids


names = []
winners = []
last_numbers = []


def play_bingo(numbers, play_grids):

    play_grids = play_grids.copy()

    for number in numbers:
        for grid_name, grid in play_grids.items():

            for row_index in range(0, len(grid)):
                play_grids[grid_name][row_index] = [
                    x if x != number else "nan"
                    for x in play_grids[grid_name][row_index]
                ]

        # Check for winner
        result = check_grids(play_grids)
        for k, v in result.items():
            if not k in names:
                names.append(k)
                winners.append(v)
                last_numbers.append(number)


play_bingo(numbers, grids)

grid_name = names[-1]
winning_grid = winners[-1]
last_number = last_numbers[-1]


print(grid_name, winning_grid, last_number)
# Sum winner
def sum_winner(winner, number):

    c = 0
    for row in winner:
        for item in row:
            if item != "nan":
                c += item

    return c * number


print("Answer is: {}".format(sum_winner(winning_grid, last_number)))
