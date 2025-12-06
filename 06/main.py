data = []

with open("input.txt") as file:
    data = file.read().splitlines()


def part1():
    newlines = []
    for i in range(len(data) - 1):
        ops = [d for d in data[i].split(" ") if d]
        for o in range(len(ops)):
            if len(newlines) < o + 1:
                newlines.append([])
            if ops[o]:
                newlines[o].append(ops[o])
    operators = [d for d in data[-1].split(" ") if d]
    print(sum([eval(operators[i].join(newlines[i])) for i in range(len(operators))]))


def part2():
    operators = []
    spaces = 0
    lengths = []
    for c in data[-1]:
        if c in ["*", "+"]:
            operators.append(c)
            if spaces != 0:
                lengths.append(spaces)
                spaces = 0
        else:
            spaces += 1
    lengths.append(spaces + 1)

    # Retrieving correct number of characters
    newlines = []
    curpos = 0
    for length in lengths:
        to_app = []
        for j in range(len(data) - 1):
            num = data[j][curpos : curpos + length]
            to_app.append(num)
        curpos += length + 1
        newlines.append(to_app)

    # Rotation
    rotated = []
    for groupn, n in enumerate(newlines):
        to_app = []
        for j in range(lengths[groupn]):
            rot_num = ""
            for i in range(len(n)):
                rot_num += n[i][j]
            to_app.append(rot_num)
        rotated.append(to_app)
    print(sum([eval(operators[i].join(rotated[i])) for i in range(len(operators))]))


if __name__ == "__main__":
    part1()
    part2()
