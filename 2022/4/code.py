# Advent of code Year 2022 Day 4 solution
# Author = Andrej Kurusiov
# Date = December 2022

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    out_list = []
    for line in input_data.split('\n'):
        out_list.append(tuple(map(int, line.replace(',', '-').split('-'))))
    return out_list


def part_1(data: list[int]) -> int:
    """number of pairs that fully overlap"""
    res = 0
    for pair in data:
        a = set(range(pair[0], pair[1]+1))
        b = set(range(pair[2], pair[3]+1))
        if a.issubset(b) or b.issubset(a):
            res += 1
    return res


TEST_DATA = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
# number of pairs that fully overlap --> 2


def part_2(data: list[int]) -> int:
    """number of pairs that overlap at all."""
    res = 0
    for pair in data:
        for a in range(pair[0], pair[1]+1):
            if a in range(pair[2], pair[3]+1):
                res += 1
                break
    return res


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA     # comment out to use real data
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
