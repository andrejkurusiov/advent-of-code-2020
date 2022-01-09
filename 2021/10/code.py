# Advent of code Year 2021 Day 10 solution
# Author = Andrej Kurusiov
# Date = December 2021

from statistics import median

CHUNKS_BCK = {')': '(', ']': '[', '}': '{', '>': '<'}
POINTS1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
POINTS2 = {'(': 1, '[': 2, '{': 3, '<': 4}


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list
    input_list = input_data.split('\n')
    return input_list


def part_1(data: list[str]) -> tuple[int, list[str]]:
    """Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?"""
    found_chars = []        # illegal characters
    incomplete_chunks = []  # used in part 2
    for line in data:
        # look for closing chars backwards;
        # search for matching opening one one position -1 and if found remove it.
        # If not found => illegal char.
        newline = ''
        for char in line:
            if char in CHUNKS_BCK:
                # look for previous matching opening char in position -1 and remove it
                if newline[-1] == CHUNKS_BCK[char]:
                    newline = newline[:-1]
                else:
                    found_chars.append(char)
                    break
            else:
                newline += char
        else:   # executed if the loop exited normally, eg. without a break
            # Save incomplete lines chunks for part 2.
            incomplete_chunks.append(newline)

    return sum((POINTS1[char] for char in found_chars)), incomplete_chunks


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

# -- Part 1: 3*2+57+1197+25137 = 26397
# {([(<{}[<>[]_}_>{[]{[(<()> - Expected ], but found } instead.
# [[<[([])_)_<([[{}[[()]]] - Expected ], but found ) instead.
# [{[{({}_]_{}}([{[{{{}}([] - Expected ), but found ] instead.
# [<(<(<(<{}_)_)><([]([]() - Expected >, but found ) instead.
# <{([([[(<>()){}]_>_(<<{{ - Expected ], but found > instead.

# -- Part 2:
# [({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})] - 288957 total points.
# [(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}) - 5566 total points.
# (((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))) - 1480781 total points.
# {<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}> - 995444 total points.
# <{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}> - 294 total points.
# Middle score --> 288957.


def part_2(data: list[str]) -> int:
    """ Figure out the sequence of closing characters for incomplete lines. 
        Start with a total score of 0. Then, for each character, multiply the total score by 5
        and then increase the total score by the point value given for the character.
        Returns middle score (median of scores).
    """
    MULTIPLY_BY = 5
    incomplete_chunks = part_1(data)[1]
    scores = []
    for chunk in incomplete_chunks:
        score = 0
        # check chunks in reverse as closing ones are in that order
        for char in chunk[:: -1]:
            # no need to actually find corresponding closing chars as their score is enough
            score = score * MULTIPLY_BY + POINTS2[char]
        scores.append(score)
    return median(scores)


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)[0]))
    print("Part Two : " + str(part_2(in_data)))
