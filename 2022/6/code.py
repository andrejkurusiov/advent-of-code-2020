# Advent of code Year 2022 Day 6 solution
# Author = Andrej Kurusiov
# Date = December 2022

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def find_start(data: str, buffer: int) -> int:
    start = 0
    end = buffer
    while end < len(data):
        part = data[start:end]
        if len(part) == len(set(part)):
            return end
        else:
            start += 1
            end += 1
    return 0


def part_1(data: str) -> int:
    return find_start(data, 4)


def part_2(data: str) -> int:
    return find_start(data, 14)


TEST_DATA = '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''
# mjqjpqmgbljsphdztnvjfqwrcgsmlb
# bvwbjplbgvbhsrlpgdmjqwftvncz
# nppdvjthqldpwncqszvftbrmjlhg
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
# Part 1: 7, 5, 6, 10, 11


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA     # comment out to use real data
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
