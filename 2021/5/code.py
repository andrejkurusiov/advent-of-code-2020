# Advent of code Year 2021 Day 5 solution
# Author = Andrej Kurusiov
# Date = December 2021

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list[tuple]:
    # Parces input string to list of integers
    input_list = input_data.split('\n')
    coords = []
    for a_line in input_list:
        x1y1, x2y2 = a_line.split(' -> ')
        a_tuple = (tuple(map(int, x1y1.split(','))),
                   tuple(map(int, x2y2.split(','))))
        coords.append(a_tuple)
    return coords


def vents_diagram(input_data: list[tuple]) -> list[list[int]]:
    """ Creates a vents' diagram using only vertical or horizontal lines.
        Numbers >=0 represent vents, zeroes represent no vents.
    Args:
        input_data (list[tuple]): tuple of start/end coordinates [int]
    Returns:
        list[int]: 2D list of vents diagram
    """
    # get x_max and y_max
    x_max, y_max = 0, 0
    for four_coords in input_data:
        x1, y1 = four_coords[0]
        x2, y2 = four_coords[1]
        x_max = max(x_max, x1, x2)
        y_max = max(y_max, y1, y2)
    # define vents 2D array with max dimentions and filled with 0
    v_diag = [[0 for x in range(x_max+1)] for y in range(y_max+1)]

    return v_diag


def fill_horisontals(input_data: list[tuple], vents: list[list[int]]) -> list[list[int]]:
    for four_coords in input_data:
        x1, y1 = four_coords[0]
        x2, y2 = four_coords[1]
        # ensure x and y coordinates always grow
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        if x1 == x2:
            for y in range(y1, y2 + 1):
                vents[y][x1] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                vents[y1][x] += 1
    return vents


def fill_diagonals(input_data: list[tuple], vents: list[list[int]]) -> list[list[int]]:
    """ Check for 45-degrees line: |x1-x2|=|y1-y2| """
    for four_coords in input_data:
        x1, y1 = four_coords[0]
        x2, y2 = four_coords[1]

        if x1 == x2:
            step_x = 0
        elif x2 > x1:
            step_x = 1
        else:
            step_x = -1

        if y1 == y2:
            step_y = 0
        elif y2 > y1:
            step_y = 1
        else:
            step_y = -1

        x, y = x1, y1
        while x != x2 + step_x and y != y2 + step_y:  # add a step to take the last value
            vents[y][x] += 1
            x += step_x
            y += step_y

    return vents


def count_overlaps(vents: list[list[int]]) -> int:
    return sum(sum(list(map(lambda x: 1 if(x > 1) else 0, vent))) for vent in vents)


def part_1(input_data: list[tuple]) -> int:
    """At how many points do at least two vertical/horizontal lines overlap?
    Args:
        input_data (str): [description]
    Returns:
        int: number of overlaps (n>=2)
    """
    vents = vents_diagram(input_data)
    # fill in the coords with x1=x2 or y1=y2
    vents = fill_horisontals(input_data, vents)

    return count_overlaps(vents)


TEST_DATA_1 = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''
# only consider horizontal and vertical lines
# produced vertical/ horizontal lines diagram:
# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....
# At how many points do at least two lines overlap? --> 5.


def part_2(input_data: list[tuple]) -> int:
    """ Same as part 1, but also add 45-degrees lines.
        Check for 45-degrees line: |x1-x2|=|y1-y2|
    """
    vents = vents_diagram(input_data)
    # fill in the coords with x1=x2 or y1=y2
    vents = fill_horisontals(input_data, vents)
    # fill 45-degrees lines with |x1-x2|=|y1-y2|
    vents = fill_diagonals(input_data, vents)

    return count_overlaps(vents)


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)))
    print("Part Two : " + str(part_2(in_data)))
