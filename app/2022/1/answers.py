from common.utils import get_input


def part_1():
    e = 0
    m = e
    for x in get_input():
        if not x:
            m = max(e, m)
            e = 0
        else:
            e = e + int(x)
    print(m)

def part_2():
    elves = []
    e = 0
    for x in get_input():
        if not x:
            elves.append(e)
            e = 0
        else:
            e = e + int(x)

    elves.sort(reverse=True)
    print(sum(elves[:3]))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
