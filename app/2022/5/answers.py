from common.utils import get_input, batch
from collections import defaultdict
import re

regex = r"move (\d+) from (\d+) to (\d+)"


def build_crate_stacks(stack_move = False):
    stacks = defaultdict(list)

    is_move = False
    for line in get_input():
        if is_move:
            count, source, destination = [int(x) for x in re.search(regex, line).groups()]
            if stack_move:
                s = stacks[source][-count:]
                stacks[destination].extend(s)
                stacks[source] = stacks[source][:-count]
            else:
                for i in range(count):
                    stacks[destination].append(stacks[source].pop())

            continue
        if not line:
            for x in stacks.values():
                x.reverse()
                is_move = True
                continue

        for (index, stack) in enumerate(batch(line, 4)):
            if stack[1].isdigit():
                break
            if stack[1].isalpha():
                stacks[index + 1].append(stack[1])

    res = []
    for x in sorted(stacks.keys()):
        res.append(stacks[x].pop())

    print(''.join(res))


def part_1():
    build_crate_stacks()


def part_2():
    build_crate_stacks(True)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
