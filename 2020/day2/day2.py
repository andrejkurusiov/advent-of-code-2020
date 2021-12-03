import re

# initial data input
infilename = "./day2.txt"
with open(infilename, "r", encoding="utf-8") as file:
    inlist = [line.strip() for line in file]


# general data parsing and checking against policy routine
def parse_data(inlist, test_policy: str):
    # test_policy - string representing the name of the test policy function to be used for part 1 or 2
    # returns the number of passwords following the policy
    correct = 0  # number of correct passwords
    for text in inlist:
        match = re.search(r"(\d+)-(\d+)\s(\w):\s(\w+)", text)
        if match:
            # tuple of (fist_num, second_num, letter)
            policy = (int(match.group(1)), int(match.group(2)), match.group(3))
            psw = match.group(4)
            if eval(test_policy)(policy, psw):
                correct += 1
    return correct


# --- Part One ---

"""
Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""


def test_policy1(policy: tuple, psw: str):
    # returns True if psw according to policy
    first, last, char = policy[0], policy[1], policy[2]
    found = re.findall(f"{char}", psw)
    return len(found) in range(first, last + 1)


testinput = ("1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc")  # 2nd is invalid


def part1(inlist=testinput):
    # returns number of correct passwords
    correct = 0  # number of correct passwords
    correct = parse_data(inlist, "test_policy1")
    return correct


# --- Part Two ---
"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?
"""


def test_policy2(policy: tuple, psw: str):
    # returns True if psw according to policy
    first, last, char = policy[0] - 1, policy[1] - 1, policy[2]
    return (psw[first] == char) ^ (psw[last] == char)


testinput = ("1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc")  # only 1st is valid


def part2(inlist=testinput):
    # returns number of correct passwords
    correct = 0
    correct = parse_data(inlist, "test_policy2")
    return correct


# --- MAIN ---
if __name__ == "__main__":
    print("Part1. Number of passwords according to policy:", part1(inlist))
    print("Part2. Number of passwords according to policy:", part2(inlist))
