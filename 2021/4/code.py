# Advent of code Year 2021 Day 4 solution
# Author = Andrej Kurusiov
# Date = December 2021

ROWS_COLUMNS = 5    # number of rows and columns on a board


class Board(list):

    def __init__(self, aList, rows_columns: int = ROWS_COLUMNS):
        list.__init__(self, aList)
        self.rows_columns = rows_columns

    def __str__(self):
        return f'Board:\n{[row for row in self]}'

    def add_board_row(self, aRow: list[int]) -> None:
        if aRow:
            self.append(aRow)

    def mark_number(self, call_number: int) -> bool:
        """Marks a calling number in a board as "-1"
           and returns True if number found, otherwise False
        Args:
            call_number (int): bingo calling number
        Returns:
            bool: True if number is found on a board
        """
        found = False
        for row in self:
            # finx indexes of matching numbers in a row
            col_idxs = [idx for idx in range(
                self.rows_columns) if row[idx] == call_number]
            # change found numbers in a row to -1
            if col_idxs:
                found = True
                for idx in col_idxs:
                    row[idx] = -1
        return found

    def is_winning(self) -> bool:
        # check rows
        for row in self:
            if sum(row) == -1 * self.rows_columns:
                return True
        # check columns
        for col_idx in range(self.rows_columns):
            if sum([row[col_idx] for row in self]) == -1 * self.rows_columns:
                return True
        return False

    def score(self, call_number: int) -> int:
        """Find sum of all unmarked numbers on that board. Then, multiply that sum by the number that was just called when the board won."""
        n_sum = 0
        for row in self:
            n_sum += sum([n for n in row if n != -1])
        return n_sum * call_number


def read_file() -> str:
    with open((__file__.rstrip("code.py")+"input.txt"), 'r', encoding="utf-8") as input_file:
        input_data = input_file.read()
    return input_data


def parse_input(input_data: str) -> tuple[list[int], list[Board]]:
    """ Returns a list of bingo numbers and a list of boards """
    # add empty item to form last board properly
    input_list = input_data.split('\n') + ['\n']
    bingo_numbers = list(map(int, input_list[0].split(',')))
    boards = []
    board = Board([])
    for board_line in input_list[2:]:   # boards data starts from 3rd element
        a_line = list(map(int, board_line.split()))
        if a_line:
            board.add_board_row(a_line)
        else:
            boards.append(board)
            board = Board([])

    return bingo_numbers, boards


def part_1(bingo_numbers: list[int], boards: list[Board]) -> int:
    """The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board. Then, multiply that sum by the number that was just called when the board won.
    Args:
        r_numbers: list[int]: list of given random numbers
        boards: list of boards; each board is a 5x5 [int] list
    Returns:
        int: score of the 1st winning board
    """
    for call_number in bingo_numbers:
        for board in boards:
            if board.mark_number(call_number) and board.is_winning():
                return board.score(call_number)
    return -1


TEST_DATA_1 = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''
# third board wins first: sum 188 * call_number 24 ==> score 4512


def part_2(bingo_numbers: list[int], boards: list[Board]) -> int:
    """ Same as part 1, but figure out which board will win last and return its score."""

    # remove board numbers till only one is left
    losing_boards = [i for i in range(len(boards))]
    for call_number in bingo_numbers:
        # if last winning board exists
        if len(losing_boards) == 1:
            # the board might need more numbers to be marked before calculating the score
            if boards[losing_boards[0]].mark_number(call_number) and boards[losing_boards[0]].is_winning():
                return boards[losing_boards[0]].score(call_number)
            else:
                continue
        # temp index list as can not modify the same list losing_boards[] while going through it
        boards_won = []
        for board_idx in losing_boards:
            if boards[board_idx].mark_number(call_number) and boards[board_idx].is_winning():
                boards_won.append(board_idx)
        # remove recently won boards' indexes from losing_boards[]
        for idx in boards_won:
            losing_boards.remove(idx)

    return -1


TEST_DATA_2 = TEST_DATA_1
# Second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked.
# The second board has a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# --- MAIN ---
if __name__ == "__main__":
    in_data = read_file()
    # in_data = TEST_DATA_1
    bingo_numbers, boards = parse_input(in_data)
    print("Part One : " + str(part_1(bingo_numbers, boards)))
    print("Part Two : " + str(part_2(bingo_numbers, boards)))
