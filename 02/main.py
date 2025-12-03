data = []

with open("input.txt") as file:
    data = file.read().splitlines()


def repeat(n):
    return int(str(n) * 2)


def part1():
    ranges = [[int(l.split("-")[0]), int(l.split("-")[1])] for l in data[0].split(",")]
    total = 0
    for r in ranges:
        orig = r.copy()
        if len(str([0])) % 2 != 0 and len(str(r[1])) % 2 != 0:
            continue
        if len(str(r[0])) % 2 != 0:
            r[0] = 10 ** (len(str(r[0])) + 1)
        if len(str(r[1])) % 2 != 0:
            r[1] = 10 ** (len(str(r[1])) + 1)

        s = int(str(r[0])[: len(str(r[0])) // 2])
        e = int(str(r[1])[: len(str(r[1])) // 2])
        for i in range(s, e + 1):
            g = repeat(i)
            if g >= orig[0] and g <= orig[1]:
                print(orig, g)
                total += g

    print(total)


def part1():
    ranges = [[int(l.split("-")[0]), int(l.split("-")[1])] for l in data[0].split(",")]
    tot = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            if (
                len(str(i)) % 2 == 0
                and str(i)[: len(str(i)) // 2] == str(i)[len(str(i)) // 2 :]
            ):
                tot += i

    print(tot)


def rshift(n):
    return str(n)[1:] + str(n)[0]


def part2():
    ranges = [[int(l.split("-")[0]), int(l.split("-")[1])] for l in data[0].split(",")]
    nums = set({})
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            n = str(i)
            for o in range(len(str(i)) - 1):
                n = rshift(n)
                if n == str(i):
                    nums.add(i)
    print(sum(nums))


if __name__ == "__main__":
    part1()
    part2()
