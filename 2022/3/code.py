# Advent of code Year 2022 Day 3 solution
# Author = Andrej Kurusiov
# Date = December 2022

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    input_list = input_data.split('\n')
    list_out = []
    for line in input_list:
        # Use ord() and an offset to obtain character priority depending on upper/lower case
        list_out.append(
            list(map(lambda x: ord(x)-38 if x.isupper() else ord(x)-96, line)))
    return list_out


def part_1(data: list[int]) -> int:
    res = 0
    for line in data:
        res += sum(set(line[:len(line)//2]) & set(line[len(line)//2:]))
    return res


TEST_DATA = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


def part_2(data: list[int]) -> int:
    N_TH = 3
    res = 0
    a_set = set()
    for order, line in enumerate(data):
        a_set = a_set.intersection(set(line)) if a_set else set(line)
        if (order+1) % N_TH == 0:
            res += sum(a_set)
            a_set.clear()
    return res


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA     # comment out to use real data
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
