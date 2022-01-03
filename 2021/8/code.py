# Advent of code Year 2021 Day 8 solution
# Author = Andrej Kurusiov
# Date = December 2021


# Digits encoding
ONE = set('cf')
FOUR = set('bcdf')
SEVEN = set('acf')
EIGHT = set('abcdefg')
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
    easy_list = [len(item) for item in EASY_NUMBERS]
    times = 0
    for line in data:
        r_lst = line[-1]
        for item in r_lst:
            if len(item) in easy_list:
                times += 1
    return times


TEST_DATA_1 = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
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


def part_2(data: list[tuple]) -> str:
    return 'not implemented'
    # known: 1, 4, 7, 8
    # 8 - 7 => 6
    # ? 2, 3, 5, 9, 0


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
