# Advent of code Year 2021 Day 2 solution
# Author = Andrej Kurusiov
# Date = December 2021


def read_file() -> str:
    with open(
        (__file__.rstrip("code.py") + "input.txt"), "r", encoding="utf-8"
    ) as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split("\n")
    # return list of tuples (str, int)
    return [(item.split()[0], int(item.split()[1])) for item in input_list]


def part_1(input_data: str) -> int:
    """What do you get if you multiply your final horizontal position by your final depth?
    Returns:
        int: [final horizontal position * final depth]
    """
    h_pos, depth = 0, 0  # Your horizontal position and depth both start at 0.
    commands = parse_input(input_data)
    for command, value in commands:
        if command == "forward":
            h_pos += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value
        else:
            print(f"ERROR: unrecognised command ({command})")
            break

    return h_pos * depth


TEST_DATA_1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
# --> 150


def part_2(input_data: str) -> int:
    """Need to rack an 'aim'.
    Commands mean different:
        down X increases your aim by X units.
        up X decreases your aim by X units.
        forward X does two things:
            It increases your horizontal position by X units.
            It increases your depth by your aim multiplied by X.
    """
    h_pos, depth, aim = 0, 0, 0
    commands = parse_input(input_data)
    for command, value in commands:
        if command == "forward":
            h_pos += value
            depth += aim * value
        elif command == "up":
            aim -= value
        elif command == "down":
            aim += value
        else:
            print(f"ERROR: unrecognised command ({command})")
            break

    return h_pos * depth


TEST_DATA_2 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
# --> 900


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    print("Part One : " + str(part_1(in_data)))
    # in_data = TEST_DATA_2
    print("Part Two : " + str(part_2(in_data)))
