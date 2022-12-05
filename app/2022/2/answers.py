from common.utils import get_input
from functools import reduce

# A/X = Rock: 1
# B/Y = Paper: 2
# C/Z = Scissors: 3

# Loss = 0
# draw = 3
# Win = 6
score_dict_1 = {
    ('A', 'X'): 4,
    ('B', 'X'): 1,
    ('C', 'X'): 7,
    ('A', 'Y'): 8,
    ('B', 'Y'): 5,
    ('C', 'Y'): 2,
    ('A', 'Z'): 3,
    ('B', 'Z'): 9,
    ('C', 'Z'): 6
}

# X = Lose
# Y = Draw
# Z = Win
score_dict_2 = {
    ('A', 'X'): score_dict_1[('A', 'Z')],
    ('B', 'X'): score_dict_1[('B', 'X')],
    ('C', 'X'): score_dict_1[('C', 'Y')],
    ('A', 'Y'): score_dict_1[('A', 'X')],
    ('B', 'Y'): score_dict_1[('B', 'Y')],
    ('C', 'Y'): score_dict_1[('C', 'Z')],
    ('A', 'Z'): score_dict_1[('A', 'Y')],
    ('B', 'Z'): score_dict_1[('B', 'Z')],
    ('C', 'Z'): score_dict_1[('C', 'X')],
}


def part_1():
    print(reduce(lambda a, b: a + b, map(lambda x: score_dict_1[tuple(x.split())], get_input())))


def part_2():
    print(reduce(lambda a, b: a + b, map(lambda x: score_dict_2[tuple(x.split())], get_input())))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
