# Advent of code Year 2022 Day 2 solution
# Author = Andrej Kurusiov
# Date = December 2022


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of tuples of strings
    input_list = input_data.split('\n')
    out_data = []
    for inp in input_list:
        turn = (inp[0], inp[-1])
        out_data.append(turn)
    return out_data


def round_res_1(elf: str, you: str) -> int:
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    pick_values = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    elf_int = pick_values.get(elf, 0)
    you_int = pick_values.get(you, 0)
    if elf_int == you_int:
        return 3 + you_int
    # win: 1 2, 2 3, 3 1
    elif (elf == 'A' and you == 'Y' or elf == 'B' and you == 'Z' or elf == 'C' and you == 'X'):
        return 6 + you_int
    else:
        return 0 + you_int


def part_1(data: list[tuple]) -> int:
    # Elf: A for Rock, B for Paper, and C for Scissors.
    # You: X for Rock, Y for Paper, and Z for Scissors.
    res = 0
    for elf, you in data:
        res += round_res_1(elf, you)
    return res


TEST_DATA = '''A Y
B X
C Z'''
# What would your total score be if everything goes
# exactly according to your strategy guide?


def round_res_2(elf: str, you: str) -> int:
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    pick_values = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
    elf_int = pick_values.get(elf, 0)
    you_int = pick_values.get(you, 0)
    if you_int == 3:    # draw
        you_pick = elf_int
    elif you_int == 6:  # win 1 2, 2 3, 3 1
        if elf_int == 1: you_pick = 2
        elif elf_int == 2: you_pick = 3
        else: you_pick = 1
    else: # lose 1 3, 2 1, 3 2
        if elf_int == 1: you_pick = 3
        elif elf_int == 2: you_pick = 1
        else: you_pick = 2
    return you_int + you_pick


def part_2(data: list[tuple]) -> int:
    # Elf: A for Rock, B for Paper, and C for Scissors.
    # X you need to lose, Y you need to draw, Z you need to win.
    res = 0
    for elf, you in data:
        res += round_res_2(elf, you)
    return res


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA     # comment out to use real data
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
