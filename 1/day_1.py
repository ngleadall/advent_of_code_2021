import sys

f = open(sys.argv[1])
inputs = [int(i) for i in f.readlines()]

c = 0
for i in range(1, len(inputs)):

    if inputs[i - 1] < inputs[i]:
        c += 1

print("Number of increases: {}".format(c))


wc = 0
for i in range(3, len(inputs)):

    if sum(inputs[i-2: i+1]) > sum(inputs[i-3: i]):
        wc += 1

print("Number of window increases: {}".format(wc))
