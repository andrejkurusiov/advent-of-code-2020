# Advent of code Year 2021 Day 8 solution
# Author = Andrej Kurusiov
# Date = December 2021


# Digits encoding - legths of known digits
ONE = 2  # set('cf')
FOUR = 4  # set('bcdf')
SEVEN = 3  # set('acf')
EIGHT = 7  # set('abcdefg')
EASY_NUMBERS = (ONE, FOUR, SEVEN, EIGHT)


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    data = []
    for line in input_list:
        left_str, right_str = line.split(" | ")
        left_lst = left_str.split()
        right_lst = right_str.split()
        l_part = [set(item) for item in left_lst]
        r_part = [set(item) for item in right_lst]
        data.append((l_part, r_part))
    return data


def part_1(data: list[tuple]) -> int:
    """ In the output values, how many times do digits 1, 4, 7, or 8 appear?"""
    # It goes down to counting how many times there come outputs with 2, 4, 3 or 8 items.
    times = 0
    for line in data:
        r_lst = line[-1]
        for item in r_lst:
            if len(item) in EASY_NUMBERS:
                times += 1
    return times


TEST_DATA = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''
# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments.


def part_2(data: list[tuple]) -> int:
    """ What do you get if you add up all of the output values?
        Output value's digits are made up of each number in output. """
    # known: 1, 4, 7, 8
    output_sum = 0
    for line in data:
        digits = [None] * 10    # each index represents one digit
        l_lst, r_lst = line
        # find easy numbers (ONE, FOUR, SEVEN, EIGHT) by their segments length
        digits[1] = list(filter(lambda x: len(x) == ONE, l_lst))[0]  # one
        digits[4] = list(filter(lambda x: len(x) == FOUR, l_lst))[0]  # four
        digits[7] = list(filter(lambda x: len(x) == SEVEN, l_lst))[0]  # seven
        digits[8] = list(filter(lambda x: len(x) == EIGHT, l_lst))[0]  # eight
        # find three
        digits[3] = list(filter(lambda x: x >= digits[1]
                         and len(x) == 5, l_lst))[0]
        # find nine
        digits[9] = list(filter(lambda x: x >= digits[4]
                         and len(x) == 6, l_lst))[0]
        # find five
        digits[5] = list(filter(lambda x: len(digits[9] - x) == 1
                         and len(x) == 5 and x not in digits, l_lst))[0]
        # find two
        digits[2] = list(filter(lambda x: len(x) == 5
                         and x not in digits, l_lst))[0]
        # find six
        digits[6] = list(filter(lambda x: len(x - digits[5]) == 1
                         and len(x) == 6 and x not in digits, l_lst))[0]
        # find zero
        digits[0] = list(filter(lambda x: x not in digits, l_lst))[0]

        number_out = 0
        for item in r_lst:
            number_out = number_out * 10 + digits.index(item)
        output_sum += number_out

    return output_sum


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
