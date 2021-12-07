import sys
import numpy as np


input = np.array([int(i) for i in open(sys.argv[1]).readline().strip().split(",")])

##########
# Part 1
##########
# moves = int(np.sum(abs(input - np.median(input))))
# print( moves )

##########
# Part 2
##########

centre = round(np.mean(input)) - 1
moves = ((np.abs(input - centre) / 2) * (np.abs(input - centre) + 1)).sum()

print(int(moves))
