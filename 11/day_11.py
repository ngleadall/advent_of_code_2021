import sys


grid = [[int(i) for i in line.strip()] for line in open(sys.argv[1]).readlines()]
rows = len(grid)
cols = len(grid[0])


answer = 0


def flash(r, c):
    global answer
    answer += 1
    grid[r][c] = -1

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:

            rr = r + dr
            cc = c + dc

            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] != -1:
                grid[rr][cc] += 1
                if grid[rr][cc] >= 10:
                    flash(rr, cc)


day = 0
while True:
    day += 1
    for row in range(rows):
        for column in range(cols):
            grid[row][column] += 1

    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == 10:
                flash(row, column)
    done_flashing = True

    for row in range(rows):
        for column in range(cols):
            if grid[row][column] == -1:
                grid[row][column] = 0
            else:
                done_flashing = False
    if day == 100:
        print(answer)
    if done_flashing:
        print(day)
        break
