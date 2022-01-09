# Advent of code Year 2021 Day 10 solution
# Author = Andrej Kurusiov
# Date = December 2021

CHUNKS = {')': '(', ']': '[', '}': '{', '>': '<'}
POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list
    input_list = input_data.split('\n')
    return input_list


def part_1(data: list[str]) -> int:
    """Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?"""
    found_chars = []
    for line in data:
        # look for closing chars backwards; count the number of the same chars,
        # search for matching opening one which equals the number of closing ones.
        # If not found the same number of opening chars => illegal char.
        newline = ''
        for i, char in enumerate(line):
            if char in CHUNKS:
                # look for previous matching opening char in position -1 and remove both
                if newline[-1] == CHUNKS[char]:
                    newline = newline[:-1]
                else:
                    found_chars.append(char)
                    break
            else:
                newline += char
    return sum((POINTS[char] for char in found_chars))


TEST_DATA = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''
# Part 1: 3*2+57+1197+25137 = 26397
# {([(<{}[<>[]_}_>{[]{[(<()> - Expected ], but found } instead.
# [[<[([])_)_<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}_]_{}}([{[{{{}}([] - Expected ), but found ] instead.
# [<(<(<(<{}_)_)><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]_>_(<<{{ - Expected ], but found > instead.


def part_2(data: list[str]) -> int:
    pass


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    in_data = TEST_DATA
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
