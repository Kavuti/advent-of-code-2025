from collections import defaultdict
from functools import lru_cache

data = []

with open("input.txt") as file:
    data = file.read().splitlines()

tachyons = []
splitters = []
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == "S":
            tachyons.append((i, j))
        elif c == "^":
            splitters.append((i, j))

splitters_idx = defaultdict(list)
[splitters_idx[s[0]].append(s[1]) for s in splitters]

history = []


def part1_and_2():
    global tachyons
    global history
    original = tachyons[0]
    clock = tachyons[0][0]
    splits = 0
    while clock < len(data):
        clock += 1
        if clock in splitters_idx:
            new_tachyons = []
            for t in tachyons:
                if t[1] in splitters_idx[clock]:
                    new_tachyons += [(clock, t[1] - 1), (clock, t[1] + 1)]
                    splits += 1
                else:
                    new_tachyons.append((clock, t[1]))
            tachyons = sorted(list(set(new_tachyons)))
        else:
            new_tachyons = []
            for t in tachyons:
                new_tachyons.append((clock, t[1]))
            tachyons = sorted(list(set(new_tachyons)))
        history.append(tachyons.copy())
    print(splits)
    print(move(original[0], original[1]))


@lru_cache(maxsize=None)
def move(x, y):
    if x == len(data) - 1:
        return 1
    elif (x + 1, y) in history[x]:
        return move(x + 1, y)
    else:
        tot = 0
        if (x + 1, y - 1) in history[x]:
            tot += move(x + 1, y - 1)
        if (x + 1, y + 1) in history[x]:
            tot += move(x + 1, y + 1)
        return tot


if __name__ == "__main__":
    part1_and_2()
