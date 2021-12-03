# initial data input
infilename = "./day9.txt"


def readfile() -> list:
    with open(infilename, "rt", encoding="utf-8") as file:
        inlist = [line.strip() for line in file]
    return inlist


def parse_input(inlist=readfile()) -> list:
    return list(map(int, inlist))


# --- Part One ---

"""
Upon connection, the port outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you, is an old cypher with an important weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.

For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid, the next number must be the sum of two of those numbers:

26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
49 would be a valid next number, as it is the sum of 24 and 25.
100 would not be valid; no two of the previous 25 numbers sum to 100.
50 would also not be valid; although 25 appears in the previous 25 numbers, the two numbers in the pair must be different.

Suppose the 26th number is 45, and the first number (no longer an option, as it is more than 25 numbers ago) was 20. Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to it:

26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
65 would not be valid, as no two of the available numbers sum to it.
64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.

Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is 127.

The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?
"""


# part 1 test input (preamble=5):
# ==> 127
testinput1 = '''35,
20,
15,
25,
47,
40,
62,
55,
65,
95,
102,
117,
150,
182,
127,
219,
299,
277,
309,
576'''.split(',\n')


def part1(inlist: list, preamble: int = 25) -> int:
    # returns first number after preamble which is not the sum of 2 numbers in preamble-size range of previous numbers
    data = parse_input(inlist)

    def from_pream(tnum: int, nums: list) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == tnum:
                    return True
        return False

    prem_start = 0
    for idx in range(preamble, len(data)):
        testnum = data[idx]
        if not from_pream(testnum, data[prem_start: prem_start+preamble]):
            return testnum
        else:
            prem_start += 1
    return -1


# --- Part Two ---
"""
You must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""


# part 2 test input:
# ==> [15, 5, 47, 40] --> 15+47 = 62.
testinput2 = testinput1


def part2(num: int, inlist: list) -> int:
    data = parse_input(inlist)
    pass
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            summa = sum(data[i:j])
            if summa == num:
                # return sum of min and max int from the range
                return(min(data[i:j]) + max(data[i:j]))
            elif summa > num:
                break
    return -1


# --- MAIN ---
if __name__ == "__main__":
    # if no parameter for part X - test input is used
    indata = readfile()
    preamble = 25
    p1 = part1(indata, preamble)
    print(
        f"Part1. The first number in the list (after the preamble) which is not the sum of two of the {preamble} numbers before it:", p1)
    # indata = testinput2
    print("Part2. Encryption weakness:", part2(p1, indata))
