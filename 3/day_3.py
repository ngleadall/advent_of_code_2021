import sys

with open(sys.argv[1], "r") as f:
    l = [[int(num) for num in line.strip()] for line in f]


def mostCommon(lst):

    zero = 0
    one = 0
    for i in lst:
        if i == 0:
            zero += 1

        else:
            one += 1

    if zero > one:
        return 0
    else:
        return 1


def decimal(binary):
    return sum(val * (2 ** idx) for idx, val in enumerate(reversed(binary)))


def oxygen(lst):

    for index in range(0, len(lst[0])):

        bits_at_index = [i[index] for i in lst]

        # Look for oxygen
        o = mostCommon(bits_at_index)

        lst = [i for i in lst if i[index] == o]

        if len(lst) == 1:
            return lst


def co2(lst):
    for index in range(0, len(lst[0])):

        bits_at_index = [i[index] for i in lst]

        # Look for oxygen
        o = 1 - mostCommon(bits_at_index)

        lst = [i for i in lst if i[index] == o]

        if len(lst) == 1:
            return lst


oxygen_number = decimal(oxygen(l)[0])
co2_number = decimal(co2(l)[0])

print(
    "Oxygen: {} , Co2: {} , Answer: {} ".format(
        oxygen_number, co2_number, oxygen_number * co2_number
    )
)
