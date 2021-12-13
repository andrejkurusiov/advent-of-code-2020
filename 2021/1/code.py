# Advent of code Year 2021 Day 1 solution
# Author = Andrej Kurusiov
# Date = December 2021


def read_file() -> list[int]:
    with open(
        (__file__.rstrip("code.py") + "input.txt"), "r", encoding="utf-8"
    ) as input_file:
        input_data = input_file.read()
    input_list = input_data.split("\n")
    return list(map(int, input_list))


def part_1(input_data: list[int]) -> int:
    """Count the number of times a depth measurement increases from the previous measurement.
    Args:
        input_data (str): depths
    Returns:
        int: number of depth increases
    """

    inc_count = 0
    for i, depth in enumerate(input_data):
        if i != 0 and input_data[i] > input_data[i - 1]:
            inc_count += 1
    return inc_count


def part_2(input_data: list[int]) -> int:
    """Consider sums of a three-measurement sliding window. Count the number of times the sum of measurements in this sliding window increases from the previous sum.
    Args:
        input_data (list[str]): depths
    Returns:
        int: number of increases
    """
    N = 3  # the "length" of the sliding window
    n_window_lst = []
    # form a list of three-measurement sliding window sums
    for i in range(0, len(input_data) - N + 1):
        n_window_lst.append(sum(input_data[i : i + N]))
    # process n_window_lst as basic case in Part 1
    return part_1(n_window_lst)


test_data_2 = """199
200
208
210
200
207
240
269
260
263"""
# --> 5

# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    print("Part One : " + str(part_1(in_data)))
    # in_data = list(map(int, test_data_2.split("\n")))
    print("Part Two : " + str(part_2(in_data)))
