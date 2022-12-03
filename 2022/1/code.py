# pylint: disable=missing-docstring

# Advent of code Year 2022 Day 1 solution
# Author = Andrej Kurusiov
# Date = December 2022

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list[str]:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    return input_list


TEST_DATA = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''
# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total? --> 45000


def part_1(data: list[str]) -> int:

    total: int = 0
    out_list = []
    for ch in data:
        if not ch:
            out_list.append(total)
            total = 0
        else:
            total += int(ch)
    out_list.append(total)  # appending the last element
    return max(out_list)


def part_2(data: list[str], top_x=3) -> int:
    total: int = 0
    top_x_list = []
    for ch in data:
        if not ch:
            top_x_list.append(total)
            total = 0
        else:
            total += int(ch)
    top_x_list.append(total)  # appending the last element
    max3 = 0
    for _ in range(top_x):
        max3 += max(top_x_list)
        top_x_list.remove(max(top_x_list))
    return max3


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA     # comment out to use real data
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
