# Advent of code Year 2021 Day 9 solution
# Author = Andrej Kurusiov
# Date = December 2021

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list[list[int]]:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    field = []
    for line in input_list:
        line_lst = [int(x) for x in line]
        field.append(line_lst)
    return field


def min_of_four(field: list[list[int]], i: int, j: int) -> int:
    """ Returns min value of 4 adjascent cells """
    comp_lst = []
    # left
    if j-1 >= 0:
        comp_lst.append(field[i][j-1])
    # up
    if i-1 >= 0:
        comp_lst.append(field[i-1][j])
    # right
    if j+1 < len(field[0]):
        comp_lst.append(field[i][j+1])
    # down
    if i+1 < len(field):
        comp_lst.append(field[i+1][j])

    return min(comp_lst)


def part_1(field: list[list[int]]) -> int:
    """ The risk level of a low point is 1 plus its height.
        What is the sum of the risk levels of all low points on your heightmap? """
    rows = len(field)
    columns = len(field[0])
    risk_lvl = 0
    for i in range(rows):
        for j in range(columns):
            tst = field[i][j]
            if tst < min_of_four(field, i, j):
                risk_lvl += tst + 1
    return risk_lvl


TEST_DATA = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)


def part_2(input_data: str) -> int:
    pass


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
