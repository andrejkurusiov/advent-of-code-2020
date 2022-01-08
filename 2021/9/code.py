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


def part_1(field: list[list[int]]) -> tuple[int, list[tuple[int, int, int]]]:
    """ The risk level of a low point is 1 plus its height.
        What is the sum of the risk levels of all low points on your heightmap? """
    rows = len(field)
    columns = len(field[0])
    low_points = []
    risk_lvl = 0
    for i in range(rows):
        for j in range(columns):
            tst = field[i][j]
            if tst < min_of_four(field, i, j):
                risk_lvl += tst + 1
                low_points.append((i, j, tst))
    return (risk_lvl, low_points)


TEST_DATA = '''2199943210
3987894921
9856789892
8767896789
9899965678'''
# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)


def explore_basin(field: list[list[int]], i: int, j: int, visited_nodes: list[tuple[int, int]], i_max: int, j_max: int) -> list:
    """Recurses to explore and form basins.
        Args:
            field (list[list[int]]): initial array of depths
            i (int): row
            j (int): column
            visited_nodes (list[tuple[int, int]]): list of already visited nodes
            i_max (int): max index of row
            j_max (int): max index of column

        Returns:
            list: visited_nodes[] list of coordinates (tuple[int, int])
    """
    # node outside of a min/max index, of value 9, or was visited --> exit recursion
    if (i in range(0, i_max) and j in range(0, j_max) and field[i][j] != 9 and (i, j) not in visited_nodes):
        visited_nodes.append((i, j))
        # check nodes around the current one
        explore_basin(field, i+1, j, visited_nodes, i_max, j_max)
        explore_basin(field, i-1, j, visited_nodes, i_max, j_max)
        explore_basin(field, i, j+1, visited_nodes, i_max, j_max)
        explore_basin(field, i, j-1, visited_nodes, i_max, j_max)

        return visited_nodes


def part_2(field: list[list[int]]) -> int:
    """ What do you get if you multiply together the sizes of the three largest basins?
        Uses already identified low points from Part_1 and explores basins around them. """
    basins = []  # list of basin lengths (int)
    i_max = len(field)
    j_max = len(field[0])
    low_points = part_1(field)[1]

    # for each low point explore its basin and add its length to basins[]
    for i, j, _ in low_points:
        visited = []
        basins.append(len(explore_basin(
            field, i, j, visited, i_max, j_max)))

    basins.sort(reverse=True)
    return (basins[0] * basins[1] * basins[2])


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data)[0]))
    print("Part Two : " + str(part_2(in_data)))
