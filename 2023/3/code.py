# -*- coding: utf-8 -*-
# Advent of code Year 2023 Day 3 solution
# Author = Andrej Kurusiov
# Date = December 2023


def read_file() -> str:
    with open(
        (__file__.rstrip('code.py') + 'input.txt'), 'r', encoding='utf-8'
    ) as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to a list of strings
    input_list = input_data.split('\n')
    return input_list


def check_adjacent_cells1(matrix: list, i: int, j: int):
    """
    Parameters:
        matrix (list): 2D list
        i (int): row index of the current cell
        j (int): column index of the current cell

    Returns:
        bool: True if a special symbol (non-alphanumeric character) is found in adjacent cells, False otherwise

    This function checks if any of the adjacent cells (up, down, left, right, up-left, up-right, down-left, down-right) of the current cell contains a special symbol (non-alphanumeric character). A special symbol is defined as any character that is not a digit or a dot ('.'). The function returns True if a special symbol is found, False otherwise.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    adjacent_cells = [
        (i - 1, j - 1),  # top-left
        (i - 1, j),  # top
        (i - 1, j + 1),  # top-right
        (i, j - 1),  # left
        (i, j + 1),  # right
        (i + 1, j - 1),  # bottom-left
        (i + 1, j),  # bottom
        (i + 1, j + 1),  # bottom-right
    ]

    for x, y in adjacent_cells:
        if 0 <= x < rows and 0 <= y < cols:
            if matrix[x][y] not in '01234567890.':
                return True
    return False


def part_1(data: list[str]) -> int:
    """any number adjacent to a symbol, even diagonally, is a "part number".
    Periods (.) do not count as a symbol.
    What is the sum of all of the part numbers in the engine schematic?"""

    rows = len(data)
    cols = len(data[0])
    sum_of_part_numbers = 0
    for row in range(rows):
        num_found = ''
        num_siuts = False
        for column in range(cols):
            ch = data[row][column]
            if ch.isdigit():
                num_found += ch
                num_siuts = num_siuts or check_adjacent_cells1(data, row, column)
            if not ch.isdigit() or column == cols - 1:  # also check the end of the row
                if num_siuts and num_found:
                    sum_of_part_numbers += int(num_found)
                num_found = ''
                num_siuts = False
    return sum_of_part_numbers


TEST_DATA = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
# not part numbers: 114 (top right) and 58 (middle right)
# PART 1 TEST: 4361
# PART 1: 556367
# PART 2 TEST: 467*35 + 451490 = 467835
# PART 2: 89471771


def check_adjacent_cells2(matrix: list, i: int, j: int) -> set[tuple[int, int]]:
    """
    Parameters:
        matrix (list): 2D list
        i (int): row index of the current cell
        j (int): column index of the current cell

    Returns:
        set of coordinates of adjascent '*' cells
    """
    rows = len(matrix)
    cols = len(matrix[0])

    adjacent_cells = [
        (i - 1, j - 1),  # top-left
        (i - 1, j),  # top
        (i - 1, j + 1),  # top-right
        (i, j - 1),  # left
        (i, j + 1),  # right
        (i + 1, j - 1),  # bottom-left
        (i + 1, j),  # bottom
        (i + 1, j + 1),  # bottom-right
    ]
    adjascents = set()
    for x, y in adjacent_cells:
        if 0 <= x < rows and 0 <= y < cols:
            if matrix[x][y] == '*':
                adjascents.add((x, y))
    return adjascents if adjascents != {()} else set()


def part_2(data: list[str]) -> int:
    """A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.
    What is the sum of all of the gear ratios in your engine schematic?"""

    rows = len(data)
    cols = len(data[0])
    potential_gears = (
        {}
    )  # {coord of an '*' (x, y): list of adjascent numbers[num1, num2, num3]}
    for row in range(rows):
        num_found = ''
        stars_xy_for_num = set()  # coords of adjascent '*' symbols
        for column in range(cols):
            ch = data[row][column]
            if ch.isdigit():
                num_found += ch
                stars_xy_for_num.update(check_adjacent_cells2(data, row, column))
            if (
                not ch.isdigit() or column == cols - 1
            ):  # not a numner; also check the end of the row
                if num_found and stars_xy_for_num:
                    for coord in stars_xy_for_num:
                        if potential_gears.get(coord):
                            potential_gears[coord].append(int(num_found))
                        else:
                            potential_gears[coord] = [int(num_found)]
                num_found = ''
                stars_xy_for_num = set()
    return sum(
        value[0] * value[1] for value in potential_gears.values() if len(value) == 2
    )


# --- MAIN ---
if __name__ == '__main__':
    in_data = read_file()
    # in_data = TEST_DATA  # comment out to use real data
    in_data = parse_input(in_data)
    print('Part One : ' + str(part_1(in_data)))
    print('Part Two : ' + str(part_2(in_data)))
