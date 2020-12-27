# initial data input
infilename = "./day8.txt"

# record which marks item already visited
VISIT_MARK = {"vis", 0}


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
The boot code is represented as a text file with one instruction per line of text. Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).

acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.

For example, consider the following program:
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

These instructions are visited in this order:
nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |

First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1 (acc +1) and jmp +4 sets the next instruction to the other acc +1 near the bottom. After it increases the accumulator from 1 to 2, jmp -4 executes, setting the next instruction to the only acc +3. It sets the accumulator to 5, and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the program tries to run any instruction a second time, you know it will never terminate.

Immediately before the program would run an instruction a second time, the value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
"""

# part 1 test input:
# ==> accumulator = 5 (before 1st execution of the same instruction the 2d time).
testinput1 = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]
# Resulting structure:
# [
#     {"nop": 0},
#     {"acc": 1},
#     {"jmp": 4},
#     {"acc": 3},
#     {"jmp": -3},
#     {"acc": -99},
#     {"acc": 1},
#     {"jmp": -4},
#     {"acc": 6},
# ]


def part1(inlist=testinput1) -> int:
    # returns accumulator value before first repeated instruction
    data = parse_input(inlist)
    accumulator = 0
    goto = 0
    while True:
        item = data[goto]
        goto_delta = 0
        if item == VISIT_MARK:
            break
        else:
            goto_delta = item.get("jmp", 1)
            accumulator += item.get("acc", 0)
            # if item.get("nop") != None:
            #     # print('item.get("nop")')
            #     goto_delta += 1
            # elif item.get("acc") != None:
            #     goto_delta += 1
            #     accumulator += item.get("acc")
            # elif item.get("jmp") != None:
            #     goto_delta += item.get("jmp", 0)
            data[goto] = VISIT_MARK  # alter data list so that visited item is marked
            goto += goto_delta
    return accumulator


# --- Part Two ---
"""
Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6
After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
"""


# part 2 test input:
# ==> accumulator = 8
testinput2 = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]


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
    data_sw = gen_swap(data)
    for lst in data_sw:  # go through generated lists
        data = lst.copy()
        accumulator = 0
        goto = 0
        looped = True  # mark whether list was looped or not
        while True:
            item = data[goto]
            goto_delta = 0
            if item == VISIT_MARK:
                looped = True
                break
            else:
                goto_delta = item.get("jmp", 1)
                accumulator += item.get("acc", 0)
                data[
                    goto
                ] = VISIT_MARK  # alter data list so that visited item is marked
                goto += goto_delta
                if goto == len(data):
                    looped = False
                    break
        if not looped:
            return accumulator
    return -1


# --- MAIN ---
if __name__ == "__main__":
    # if no parameter for part X - test input is used
    indata = readfile()
    print("Part1. Accumulator value before first repeated instruction:", part1(indata))
    # indata = testinput2
    print(
        "Part2. Value of the accumulator after the program terminates:", part2(indata)
    )