# Tasks from https://adventofcode.com/2020

EQUAL_TO = 2020
inputfile = "./day1.txt"

with open(inputfile, "r", encoding="utf-8") as infile:
    values = [int(line.strip()) for line in infile]

# Part 1


def part1():
    # Find the two entries that sum to 2020 and then multiply those two numbers together.

    for i, x in enumerate(values[:-2]):
        for j, y in enumerate(values[i + 1 :]):
            if x + y == EQUAL_TO:
                return ((x, y), x * y)


# Part 2


def part2():
    # Find three numbers in your expense report that meet the same criteria.
    # Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
    # In your expense report, what is the product of the three entries that sum to 2020?

    from itertools import combinations
    from math import prod

    for t3 in combinations(values, 3):
        if sum(t3) == EQUAL_TO:
            return t3, prod(t3)


# Part 1 can also be solved using part2 algorithm, left for comparison
print(part1())
print(part2())