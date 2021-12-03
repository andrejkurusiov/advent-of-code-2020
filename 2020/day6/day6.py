# initial data input
infilename = "./day6.txt"


def readfile() -> list:
    with open(infilename, "rt", encoding="utf-8") as file:
        inlist = [line.strip() for line in file]
    return inlist


def parse_input(inlist: list) -> list:
    # creates a list of sets (group answers)
    data_list = []  # list of answers
    # artificially add empty item in order to mark the end of the last document
    inlist.append("")
    group = set()
    for item in inlist:
        if item:  # not an empty line => belongs to the same group
            group.update(*item.split())
        else:  # starts new document
            data_list.append(group)
            group = set()
    return data_list


# --- Part One ---

"""
The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes".
For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:
abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""


# sum of positive unique answers: 3+3+3+1+1 = 11
testinput1 = ["abc", "", "abc", "", "abac", "", "aaaa", "", "b"]


def part1(inlist=testinput1) -> int:
    # For each group, count the number of questions to which anyone answered "yes".
    # What is the sum of those counts?
    return sum(len(answer) for answer in parse_input(inlist))


# --- Part Two ---
"""
You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which _everyone_ answered "yes"!
--
abc

a
b
c

ab
ac

a
a
a
a

b
--
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""


testinput2 = ["abc", "", "a", "b", "c", "", "ab", "ac", "", "a", "a", "a", "a", "", "b"]
# parse_input2() ->
#  [[{'c', 'a', 'b'}], [{'a'}, {'b'}, {'c'}], [{'a', 'b'}, {'c', 'a'}], [{'a'}, {'a'}, {'a'}, {'a'}], [{'b'}]]


def parse_input2(inlist: list) -> list:
    # creates a list of lists of sets (individual group answers)
    # [ [{}, {}, ..], [{}, {}, ..], [{}, {}, ..], .. ]
    data_list = []  # list of all groups
    # artificially add empty item in order to mark the end of the last document
    inlist.append("")
    group = []
    # answer = set()
    for item in inlist:
        if item:  # not an empty line => belongs to the same group
            group.append(set(item))
        else:  # starts new document
            data_list.append(group)
            group = []
    return data_list


def part2(inlist=testinput2):
    # goes list items (lists) and sets inside each internal list
    # finds intersections of sets in internal lists
    # and sums the lengths of each intersection
    sum_yes = 0
    for group in parse_input2(inlist):
        # special case as .intersection() can not be done with jus tone set
        if len(group) == 1:
            sum_yes += len(group[0])
        # find intersection of all sets in an internal list if list > 1 set
        elif len(group) > 1:
            yes = group[0]
            for item in group[1:]:
                yes = yes.intersection(item)
            sum_yes += len(yes)
    return sum_yes


# --- MAIN ---
if __name__ == "__main__":
    # if no parameter for part X - test input is used
    print("Part1. Sum of positive unique answers:", part1(readfile()))
    print(
        "Part2. Sum of the number of questions to which everyone answered 'yes':",
        part2(readfile()),
    )
