# -*- coding: utf-8 -*-
#
# Advent of code: Year 2023 Day 5 solution
# Author = Andrej Kurusiov
# Date = December 2023


def read_file() -> str:
    with open(
        file=(__file__.rstrip('code.py') + 'input.txt'), mode='r', encoding='utf-8'
    ) as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    return input_data.split('\n')


def part_1(data: list) -> int:
    """Each line within a map contains three numbers: the destination range start,
    the source range start, and the range length.
    Any source numbers that aren't mapped correspond to the same destination number.
    Find the lowest location number that corresponds to any of the initial seeds.
    """
    # Extract initial items from the first line
    items = [int(x) for x in data[0].split(':')[-1].split()]
    changed = [False] * len(items)

    for line in data[1:]:
        if line and line[0].isdigit():
            dest, src, leng = map(int, line.split())

            for i, item in enumerate(items):
                if not changed[i] and item in range(src, src + leng):
                    items[i] += dest - src
                    changed[i] = True
        else:
            # Reset the changed list when a new mapping starts
            changed = [False] * len(items)
    return min(items)


TEST_DATA = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

""" PART 1 TEST ==> 35
    Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
    The lowest location number is 35.
    PART 1 RESULTS ==> 157211394."""


def part_2(data: list[str]) -> int:
    pass


# --- MAIN ---
if __name__ == '__main__':
    in_data = read_file()
    # in_data = TEST_DATA  # comment out to use real data
    in_data = parse_input(in_data)
    print(f'Part One : {part_1(in_data)}')
    print(f'Part Two : {part_2(in_data)}')
