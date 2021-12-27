# Advent of code Year 2021 Day 6 solution
# Author = Andrej Kurusiov
# Date = December 2021

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.split(',')
    return list(map(int, input_list))


def part_1(fishes: list[int], days: int) -> int:
    """Each day, a 0 becomes a 6 and adds a new 8 to the end of the list, while each other number decreases by 1 if it was present at the start of the day.
    How many lanternfish would there be after 80 days?
    Args:
        input_data (list[int]): initial list of fishes
        days (int): number of days to check
    Returns:
        int: number of fishes at the end of <days> days cycle
    """

    ZERO_REVERTS_TO = 6
    NEW_FISH = 8

    # frequency array for fishes, indexes correspond to the number of days until it creates a new fish.
    fish_freq = [0] * (NEW_FISH + 1)
    for fnum in range(NEW_FISH + 1):
        fish_freq[fnum] += fishes.count(fnum)

    for _ in range(days):
        add_fishes = fish_freq[0]
        for fnum in range(NEW_FISH):
            fish_freq[fnum] = fish_freq[fnum + 1]
        fish_freq[ZERO_REVERTS_TO] += add_fishes
        fish_freq[NEW_FISH] = add_fishes

    return sum(fish_freq)


TEST_DATA_1 = '''3,4,3,1,2'''
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# ...
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
# After 80 days ==> 5934.


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    in_data = parse_input(in_data)
    print("Part One : " + str(part_1(in_data, 80)))
    print("Part Two : " + str(part_1(in_data, 256)))
