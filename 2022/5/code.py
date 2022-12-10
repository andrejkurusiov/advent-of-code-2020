# Advent of code Year 2022 Day 5 solution
# Author = Andrej Kurusiov
# Date = December 2022


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> tuple:
    """Read stack data and moves to separate structures"""
    START_POS = 1
    INCREMENT = 4
    a_list = input_data.split('\n')
    # find line number with digits and the last digit => stacks dimentions
    stack_height = a_list.index('') - 1
    n_stacks = int(a_list[stack_height].split()[-1])
    # read in all stacks
    #   first read line by line, then transpose to stacks using zip()
    stacks_rows = []
    for line in range(0, stack_height):
        stack = []
        for item in range(START_POS, (n_stacks)*INCREMENT, INCREMENT):
            stack.append(a_list[line][item])
        stacks_rows.append(stack)
    # reverse stacks and remove empty (' ') items
    stacks_d = [list(reversed(a)) for a in zip(*stacks_rows)]
    stacks = []
    for stack_d in stacks_d:
        stack = [i for i in stack_d if i != ' ']
        stacks.append(stack)
    # read the moves to list of moves
    moves = []
    for line in range(stack_height+2, len(a_list)):
        move_dirty = a_list[line].split()
        moves.append(
            (int(move_dirty[1]),
             int(move_dirty[3]) - 1,
             int(move_dirty[-1]) - 1)
        )
    return stacks, moves


def part_1(stacks: list, moves: tuple[int]) -> str:
    """Crates are moved one at a time.
    What crate ends up on top of each stack?"""
    res = ''
    for move in moves:
        n_crates, src_stack, dest_stack = move  # type: ignore
        for _ in range(n_crates):
            stacks[dest_stack].append(stacks[src_stack].pop())
    for stack in stacks:
        res += stack[-1]
    return res


TEST_DATA = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
# positions of data: 2, 6, 10, 14, ...


def part_2(stacks: list, moves: tuple[int]) -> str:
    """Crane can move multiple crates at once.
       What crate ends up on top of each stack?
    """
    res = ''
    for move in moves:
        n_crates, src_stack, dest_stack = move  # type: ignore
        to_move = stacks[src_stack][-(n_crates):]
        stacks[dest_stack].extend(to_move)
        del stacks[src_stack][-(n_crates):]
    for stack in stacks:
        res += stack[-1]
    return res


# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA     # comment out to use real data
    d1, d2 = parse_input(in_data)
    print("Part One : " + str(part_1(d1, d2)))
    d1, d2 = parse_input(in_data)
    print("Part Two : " + str(part_2(d1, d2)))
