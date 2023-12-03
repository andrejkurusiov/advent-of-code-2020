# Advent of code Year 2023 Day 1 solution
# Author = Andrej Kurusiov
# Date = December 2023

import string


def read_file() -> str:
    with open(
        (__file__.rstrip("code.py") + "input.txt"), 'r', encoding="utf-8"
    ) as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    return input_list


def part_1(data: list[str]) -> int:
    n1, n2, line_num = 0, 0, 0
    for line in data:
        for ch in line:
            if ch in string.digits:
                n1 = int(ch) * 10
                break
        for ch in line[::-1]:
            if ch in string.digits:
                n2 = int(ch)
                break
        line_num += n1 + n2
    return line_num


TEST_DATA = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''


def part_2(data: list[str]) -> int:
    spelled = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    n1, n2, line_num = 0, 0, 0
    for line in data:
        found_words_left = {line.index(s): spelled.get(s) for s in spelled.keys() if s in line}
        found_words_right = {line.rfind(s): spelled.get(s) for s in spelled.keys() if s in line}
        min_word = min(found_words_left.keys() if len(found_words_left.keys()) else [len(line), len(line)])
        max_word = max(found_words_right.keys() if len(found_words_right.keys()) else [0, 0])
        for ch in line[:min_word]:
            if ch in string.digits:
                n1 = int(ch) * 10
                break
        else:
            n1 = found_words_left.get(min_word, 0) * 10
        # last digit
        for ch in reversed(line[max_word:]):
            if ch in string.digits:
                n2 = int(ch)
                break
        else:
            n2 = found_words_right.get(max_word, 0)
        line_num += n1 + n2
    return line_num


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA  # comment out to use real data
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
