from common.utils import get_input


def check_covered(rng_1, rng_2):

    x = range(rng_1[0], rng_1[1]+1)
    y = range(rng_2[0], rng_2[1]+1)

    xs = set(x)
    ys = set(y)

    return all(i in xs for i in y) or all(i in ys for i in x)


def check_overlap(rng_1, rng_2):
    x = range(rng_1[0], rng_1[1]+1)
    y = range(rng_2[0], rng_2[1]+1)

    xs = set(x)
    ys = set(y)

    return any(i in xs for i in y) or any(i in ys for i in x)


def part_1():

    count = 0
    for line in get_input():
        ranges = list(map(lambda x: tuple([int(z) for z in x.split('-')]), line.split(',')))

        if check_covered(ranges[0], ranges[1]):
            count += 1

    print(count)


def part_2():
    count = 0
    for line in get_input():
        ranges = list(map(lambda x: tuple([int(z) for z in x.split('-')]), line.split(',')))

        if check_overlap(ranges[0], ranges[1]):
            count += 1

    print(count)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
