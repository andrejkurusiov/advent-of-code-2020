# Advent of code Year 2021 Day 3 solution
# Author = Andrej Kurusiov
# Date = December 2021

def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> list:
    # Parces input string to list of integers
    input_list = input_data.strip().split('\n')
    return input_list


def binaryToDecimal(number_bin_str: str) -> int:
    return int(number_bin_str, 2)


def part_1(input_data: str) -> int:
    """Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
       Epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used.
    Args:
        input_data (str): raw input from file
    Returns:
        int: (gamma rate)*(epsilon rate), all in decimal
    """
    gamma_r, epsilon_r = 0, 0
    gamma_str, epsilon_str = '', ''
    input_arr = parse_input(input_data)
    # array to keep frequencies of 0 and 1 at position x: [{0: x, 1: y}, {}, ]
    freq_arr = [{'0': 0, '1': 0} for _ in range(len(input_arr[0]))]
    for elem in input_arr:
        for i, char in enumerate(elem):
            freq_arr[i][char] += 1
    # construct gamma and epsilon rate strings
    for dct in freq_arr:
        if dct['0'] >= dct['1']:
            gamma_str += '0'
            epsilon_str += '1'
        else:
            gamma_str += '1'
            epsilon_str += '0'
    # convert binary to int
    gamma_r = binaryToDecimal(gamma_str)
    epsilon_r = binaryToDecimal(epsilon_str)

    return gamma_r * epsilon_r


TEST_DATA_1 = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
# --> gamma rate is the binary number 10110, or 22 in decimal.
# --> the epsilon rate is 01001, or 9 in decimal.
# ==> 22*9 = 198


def freq_at_bit(in_data: list, position: int) -> tuple:
    """Returns frequency of bit '0' and '1' in the position 'position' for input data (list of str)
    Args:
        in_data (list): list of str
        position (int): position to check the bit in
    Returns:
        tuple: (int, int)
    """
    bits = [0, 0]  # frequency of '0' and '1' in corresponding positions
    for item in in_data:
        bits[int(item[position])] += 1
    return tuple(bits,)


def part_2(input_data: str) -> int:
    """life support rating = (oxygen generator rating) * (CO2 scrubber rating)
    Args:
        input_data (str): raw input from file
    Returns:
        int: life support rating (in decimal)
    """
    ox_rate, co2_rate = 0, 0
    input_arr = parse_input(input_data)
    # arrays to be filtered starting from initial array
    ox_arr = input_arr.copy()
    co2_arr = input_arr.copy()

    # going through all bits (first item taken as all same length)
    for bit_pos in range(len(input_arr[0])):
        # oxygen rate
        zeroes_ox, ones_ox = freq_at_bit(ox_arr, bit_pos)
        if len(ox_arr) > 1:
            bit_to_keep = '1' if ones_ox >= zeroes_ox else '0'
            ox_arr = list(filter(lambda x: x[bit_pos] == bit_to_keep, ox_arr))
        # co2 rate
        zeroes_co2, ones_co2 = freq_at_bit(co2_arr, bit_pos)
        if len(co2_arr) > 1:
            bit_to_keep = '0' if zeroes_co2 <= ones_co2 else '1'
            co2_arr = list(
                filter(lambda x: x[bit_pos] == bit_to_keep, co2_arr))

    ox_rate = binaryToDecimal(ox_arr[0])
    co2_rate = binaryToDecimal(co2_arr[0])

    return ox_rate * co2_rate


TEST_DATA_2 = TEST_DATA_1
# oxygen generator rating is 10111, or 23 in decimal.
# CO2 scrubber rating is 01010, or 10 in decimal.
# ==> 23*10 = 230.

# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    print("Part One : " + str(part_1(in_data)))
    # in_data = TEST_DATA_2
    print("Part Two : " + str(part_2(in_data)))
