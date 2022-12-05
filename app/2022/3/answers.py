from functools import reduce
from typing import List, Set

from common.utils import get_input, batch
from collections import defaultdict


def priority(c: str):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38


def score(itr: Set):
    return sum(map(lambda x: priority(x), itr))


class Rucksack:
    def __init__(self, input):
        self.left = Compartment(input[:int(len(input) / 2)])
        self.right = Compartment(input[int(len(input) / 2):])

    def priority_intersection(self):
        intersection = self.left.uniqueChars.intersection(self.right.uniqueChars)
        #print(f"Intersection is {intersection}")
        return score(intersection)





class Compartment:
    def __init__(self, input):
        self.count_dict = defaultdict(int)
        for x in input:
            self.count_dict[x] += 1

        self.uniqueChars = set(input)


def part_1():
    print(sum(map(lambda y: y.priority_intersection(), [Rucksack(x) for x in get_input()])))


def part_2():
    tmp = []
    for coll in batch(get_input(), 3):
        tmp.append(score(reduce(lambda x, y: x.intersection(y), map(lambda q: set(q), coll))))

    print(sum(tmp))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
