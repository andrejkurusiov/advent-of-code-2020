# initial data input
infilename = "./day9.txt"


def readfile():
    with open(infilename, "rt", encoding="utf-8") as file:
        inlist = [line.strip() for line in file]
    return inlist


def parse_input(inlist=readfile()):
    data_list = []  # list of dics of form {"abc": integer}
    data_list = [{item[:3]: int(item[3:])} for item in inlist if item]
    return data_list


# --- Part One ---

"""
XXX
"""

# part 1 test input:
# ==> XXX
testinput1 = ["XXX"]
# Resulting structure:
# XXX


def part1(inlist=testinput1) -> int:
    # returns XXX
    data = parse_input(inlist)
    pass
    return -1


# --- Part Two ---
"""
XXX
"""


# part 2 test input:
# ==> XXX
testinput2 = ["XXX"]


def gen_swap(data: list):
    # Change exactly one jmp (to nop) or nop (to jmp)
    # Generator function
    i_prev = -1  # index of previously changed item; -1 if no change happened yet
    prev = dict()  # previous version of a dictionary
    for i, item in enumerate(data):
        val = item.get("jmp") or item.get("nop")
        if val != None:
            if i_prev != -1:
                data[i_prev] = prev
            prev = item
            i_prev = i
            (key,) = item.keys()
            key = "jmp" if key == "nop" else "nop"
            data[i] = {key: val}
            yield data


def part2(inlist=testinput2) -> int:
    data = parse_input(inlist)
    pass
    return -1


# --- MAIN ---
if __name__ == "__main__":
    # if no parameter for part X - test input is used
    indata = testinput1
    print("Part1. XXX", part1(indata))
    # indata = testinput2
    # print("Part2. XXX", part2(indata))
