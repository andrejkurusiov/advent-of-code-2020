# Advent of code Year 2021 Day 7 solution
# Author = Andrej Kurusiov
# Date = December 2021

from statistics import median as st_median
from statistics import mean as st_mean


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split(',')
    return list(map(int, input_list))


def part_1(in_positions: list[int]) -> int:
    """ Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position? """
    med_position = int(st_median(in_positions))
    fuel_total = sum(abs(med_position - position) for position in in_positions)
    return fuel_total


TEST_DATA_1 = '''16,1,2,0,4,2,7,1,2,14'''
# horizontal position that costs the least fuel is horizontal position 2: costs a total of 37 fuel.


def part_2(in_positions: list[int]) -> int:
    """ Each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on."""

    mean_position = int(st_mean(in_positions))
    # mean_position = 475 -- depends on rounding manner!
    # arithmetic sum: n*(a1+an)/2
    fuel_total = 0
    for position in in_positions:
        n = abs(mean_position - position)
        fuel_total += n * (1 + n) // 2
    return fuel_total


TEST_DATA_2 = TEST_DATA_1
# in the example above, this becomes 5
# This costs a total of 168 fuel.


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
