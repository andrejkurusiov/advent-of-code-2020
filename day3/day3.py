import re

# initial data input
infilename = "./day3.txt"
with open(infilename, "r", encoding="utf-8") as file:
    inlist = [line.strip() for line in file]


TREE = "#"

testinput = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

# --- Part One ---

"""
Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""


def slide(pattern, right: int, down: int) -> int:
    # returns the number of trees ('#') on the way
    trees = 0
    # "coordinates" on the extendable "map"; when x goes beyond, it flips to the beginning
    x, y = (
        0,
        0,
    )
    xmax = len(pattern[x])
    ymax = len(pattern)
    # print(pattern[y])
    # print(f"xmax= {xmax}, ymax= {ymax}")
    for y in range(0, ymax, down):
        # print(f"x= {x}, y= {y}")
        if pattern[y][x] == TREE:
            trees += 1
            # print("trees=", trees)
        x = (x + right) % xmax
    return trees


def part1(inlist=testinput) -> int:
    # returns number of trees on the way
    trees = slide(inlist, right=3, down=1)
    return trees


# --- Part Two ---
"""
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""


def part2(inlist=testinput) -> int:
    # returns number of trees on the way
    trajectories = frozenset(((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))
    trees_list = []
    for right, down in trajectories:
        trees_list.append(slide(inlist, right, down))
    mul_trees = 1
    for tree in trees_list:
        mul_trees *= tree
    return mul_trees


# --- MAIN ---
if __name__ == "__main__":
    print("Part1. Number of trees on the way:", part1(inlist))
    print(
        "Part2. Number of trees on the way (multiplied using different trajectories):",
        part2(inlist),
    )
