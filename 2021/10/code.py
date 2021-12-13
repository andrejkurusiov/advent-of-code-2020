# Advent of code Year 2021 Day 10 solution
# Author = Andrej Kurusiov
# Date = December 2021

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input = input_file.read()
    return input

def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    return list(map(int, input_list))


def part_1(input_data: str) -> int:
    pass


test_data_1 = '''x
y
z'''


def part_2(input_data: str) -> int:
    pass


test_data_2 = '''x
y
z'''


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    print("Part One : "+ str(part_1(in_data)))
    print("Part Two : "+ str(part_2(in_data)))