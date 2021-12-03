import re

# initial data input
infilename = "./day7.txt"


def readfile() -> list:
    with open(infilename, "rt", encoding="utf-8") as file:
        inlist = [line.strip() for line in file]
    return inlist


def parse_input1(inlist: list) -> dict:
    # creates a dictionary with key as "outser bag" and values set of "inner bags"
    # { 'outer_bag1': {bag a, bag b, ..}, 'outer_bag2': {bag c, bag d, ..}, .. }
    data_dict = {}
    # (?:re)	non-capturing group
    pat_outer_bag = re.compile(r"(\w+ \w+) bags contain")  # compile regex
    pat_inner_bags = re.compile(r" \d+ (\w+ \w+) bags?")  # compile regex
    for txt in inlist:
        outer_bag = re.search(pat_outer_bag, txt).group(1)
        # rule.append(outer_bag)
        inner_bags = re.findall(pat_inner_bags, txt)
        # rule.append(set(inner_bags))
        # data_list.append(rule)
        data_dict[outer_bag] = set(inner_bags) if inner_bags else {}
    return data_dict


# --- Part One ---

"""
For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

You have a _shiny gold_ bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?
"""


# test input for Part 1
testinput1 = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]
# { 'light red': {'bright white', 'muted yellow'},
#   'dark orange': {'bright white', 'muted yellow'},
#   'bright white': {'shiny gold'},
#   ...
#   'dotted black': {}
# }


found_outer_bags = set()  # global


def part1(inlist, mybag="shiny gold"):
    global found_outer_bags
    rules = inlist
    for outer_bag, inner_bags in rules.items():
        if mybag in inner_bags:
            # print("mybag=", mybag, "|", outer_bag, inner_bags)
            found_outer_bags.add(outer_bag)
            part1(inlist, mybag=outer_bag)

    return found_outer_bags


# --- Part Two ---
"""
Consider again your shiny gold bag and the rules from the above example:
// shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""


# Test data for part 2. Answer is 32 == (1 + 1*3 + 1*4 + 2 + 2*5 + 2*6) bags
testinput2 = [
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "faded blue bags contain 0 other bags.",
    "dotted black bags contain 0 other bags.",
    "vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.",
    "dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.",
]
# {
#     "shiny gold": {"dark red": 2},
#     "dark red": {"dark orange": 2},
#     "dark orange": {"dark yellow": 2},
#     "dark yellow": {"dark green": 2},
#     "dark green": {"dark blue": 2},
#     "dark blue": {"dark violet": 2},
#     "dark violet": {},
# }


def parse_input2(inlist: list) -> dict:
    # creates a dictionary with "outser bag" as keys and dictionary of "inner bags" as values
    # dic{ 'outer_bag1': {"bag a": n, "bag b": k, ..}, 'outer_bag2': {"bag c": n, "bag d": k, ..}, .. }
    data_dict = {}
    # (?:re)	non-capturing group
    pat_outer_bag = re.compile(r"(\w+ \w+) bags contain")  # compile regex
    pat_inner_bags = re.compile(r" (\d+) (\w+ \w+) bags?")  # compile regex
    for txt in inlist:
        outer_bag = re.search(pat_outer_bag, txt).group(1)
        inner_bags = re.findall(pat_inner_bags, txt)  ## [(n, 'bag1'), (k, 'bag2'), ...]
        inner_dic = {}
        for bag in inner_bags:
            inner_dic[bag[1]] = int(bag[0])
        data_dict[outer_bag] = inner_dic if inner_dic else {}
    return data_dict


found_inner_bags = set()
inner_bags_counts = []


def part2(rules, mybag="shiny gold"):
    global found_inner_bags
    global inner_bags_counts
    print("-" * 10)
    # print("rules:", rules)
    for outer_bag, inner_bags_dic in rules.items():
        if outer_bag == mybag:
            print("mybag=", mybag, "|", outer_bag, inner_bags_dic)
            for bag, n in inner_bags_dic.items():
                found_inner_bags.add(bag)
                # print("found_inner_bags:", found_inner_bags)
                # multi = inner_bags_counts[-1] if inner_bags_counts else 1
                # inner_bags_counts.append(n)
                print("total_inner_bags:", inner_bags_counts)
                print("bag:", bag)

                part2(rules, mybag=bag)
            inner_bags_counts.append(list(inner_bags_dic.values()))
    return inner_bags_counts


# --- MAIN ---
if __name__ == "__main__":
    part1_input = parse_input1(readfile())  # or = testinput1
    print(
        "Part1. Number of bag colors can eventually contain at least one shiny gold bag:",
        len(part1(part1_input)),
    )
    # part2_input = parse_input2(testinput2)
    # print("Part2. XXX:", part2(part2_input), sum(part2(part2_input)))
