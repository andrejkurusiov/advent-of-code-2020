# Advent of code Year 2023 Day 1 solution
# Author = Andrej Kurusiov
# Date = December 2023

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    return list(map(int, input_list))


def part_1(data: list[str]) -> int:
    pass


TEST_DATA = '''x
y
z'''


def part_2(data: list[str]) -> int:
    pass


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    in_data = TEST_DATA     # comment out to use real data
    in_data = parse_input(in_data)
    print("Part One : "+ str(part_1(in_data)))
    print("Part Two : "+ str(part_2(in_data)))