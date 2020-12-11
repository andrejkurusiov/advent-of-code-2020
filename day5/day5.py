# initial data input
infilename = "./day5.txt"

MAXROWS = 127
MAXCOLUMNS = 7


def readfile():
    with open(infilename, "rt", encoding="utf-8") as file:
        inlist = [line.strip() for line in file]
    return inlist


# --- Part One ---

"""
this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.

The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""

# For part 1:
#   BFFFBBFRRR: row 70, column 7, seat ID 567.
#   FFFBBBFRRR: row 14, column 7, seat ID 119.
#   BBFFBBFRLL: row 102, column 4, seat ID 820. <-- max seat_id

testinput1 = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def binary_choice(txt: str, smaller: str, bigger: str, maxnum: int) -> int:
    # does binary choice, where 'smaller' means smaller part, and 'bigger' - larger part of a range
    minn, maxn = 0, maxnum
    for ch in txt:
        if ch == smaller:
            maxn = minn + (maxn - minn) // 2
        elif ch == bigger:
            minn = minn + (maxn - minn) // 2 + 1
    return minn if minn == maxn else -1


def get_seat_id(ticket: str) -> int:
    # ticket example: BFFFBBFRRR
    row = binary_choice(ticket[:7], smaller="F", bigger="B", maxnum=MAXROWS)
    column = binary_choice(ticket[7:], smaller="L", bigger="R", maxnum=MAXCOLUMNS)
    seat_id = row * 8 + column
    return seat_id


def analyse(tlist: list) -> list:
    # returns a a list of seat_ids from the list of tickets
    ids = [get_seat_id(ticket) for ticket in tlist]
    return ids


def part1(inlist=testinput1) -> int:
    # returns number of highest seat_id
    return max(analyse(inlist))


# --- Part Two ---
"""
It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""


def part2(inlist=testinput1):
    # returns your seat_id
    ids = analyse(inlist)
    for id in range(min(ids), max(ids)):
        if id not in ids:
            return id
    return None


# --- MAIN ---
if __name__ == "__main__":
    # if no parameter for part X - test input is used
    print("Part1. Max seat id:", part1(readfile()))
    print("Part2. My seat id:", part2(readfile()))
