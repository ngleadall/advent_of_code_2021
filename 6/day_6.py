import sys
import numpy as np

init = np.array([int(i) for i in open(sys.argv[1]).readline().strip().split(",")])
DAYS = int(sys.argv[2])


def calculate_fish(initial_fish, days):
    fish_at_stage_count = np.zeros(9, np.uint64)
    fish_at_stage_count[:6] = np.array([np.sum(initial_fish == k) for k in range(6)])

    for day in range(days):

        zeros = fish_at_stage_count[0]
        fish_at_stage_count[:-1] = fish_at_stage_count[1:]
        fish_at_stage_count[6] += zeros
        fish_at_stage_count[8] = zeros

    return np.sum(fish_at_stage_count)


print(calculate_fish(init, DAYS))
