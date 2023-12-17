# -*- coding: utf-8 -*-
# Advent of code Year 2023 Day 4 solution
# Author = Andrej Kurusiov
# Date = December 2023

import re


def read_file() -> str:
    with open(
        (__file__.rstrip('code.py') + 'input.txt'), 'r', encoding='utf-8'
    ) as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list[tuple[set, set]]:
    # Parces input string to list of integers
    lines = input_data.split('\n')
    data_list = []
    for line in lines:
        a = set()
        b = set()
        ab = re.search(r":\s+((?:\d+\s*)+)\|\s+((?:\d+\s*)+)", line)
        if ab:
            a = set(map(int, ab.group(1).split()))
            b = set(map(int, ab.group(2).split()))
            data_list.append((a, b))
    return data_list


def part_1(data: list) -> int:
    """The first match makes the card worth one point and each match after the first doubles the point value of that card.
    How many points are they worth in total?"""
    # points = a.intersection(b) --> 2^(len(matching_elements)-1)
    res = 0
    for item in data:
        items_matching = len(item[0].intersection(item[1]))
        if items_matching:
            res += 2 ** (items_matching - 1)
    return res


TEST_DATA = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
# PART 1: 8+2+2+1+0+0 = 13 points. Answer = 20855.
# PART 2:


def part_2(data: list[str]) -> int:
    pass


# --- MAIN ---
if __name__ == '__main__':
    in_data = read_file()
    # in_data = TEST_DATA  # comment out to use real data
    in_data = parse_input(in_data)
    print('Part One : ' + str(part_1(in_data)))
    print('Part Two : ' + str(part_2(in_data)))
