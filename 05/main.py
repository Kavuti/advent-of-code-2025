data = []

with open("input.txt") as file:
    data = file.read().splitlines()

freshes = []
availables = []
for line in data:
    if "-" in line:
        a, b = line.split("-")
        freshes += [(int(a), int(b))]
    elif line:
        availables.append(int(line))

freshes = sorted(freshes)


def part1():
    fresh_n = 0
    for a in availables:
        for f in freshes:
            if f[0] <= a <= f[1]:
                fresh_n += 1
                break
    print(fresh_n)


def part2():
    global freshes
    repeat = True
    while repeat:
        repeat = False
        new_freshes = []
        i = 0
        while i < len(freshes) - 1:

            if freshes[i][1] >= freshes[i + 1][0]:
                new_freshes.append(
                    (freshes[i][0], max(freshes[i + 1][1], freshes[i][1]))
                )
                i += 1
                repeat = True
            else:
                new_freshes.append(freshes[i])
            i += 1

        if i == len(freshes) - 1:
            new_freshes.append(freshes[i])
        freshes = new_freshes.copy()

    print(sum([c[1] - c[0] + 1 for c in freshes]))


if __name__ == "__main__":
    part1()
    part2()
