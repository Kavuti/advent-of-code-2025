import re
import heapq
from functools import lru_cache
from itertools import combinations

data = []

with open("input.txt") as file:
    data = file.read().splitlines()


def get_rolls():
    rolls = []
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char == "@":
                rolls.append((i, j))
    return rolls


def get_accessibles(rolls):
    accessible = []

    for r in rolls:
        poss = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        c = 0
        for p in poss:
            rn = (r[0] + p[0], r[1] + p[1])
            if 0 <= rn[0] < len(data) and 0 <= rn[1] < len(data[0]) and rn in rolls:
                c += 1
        if c < 4:
            accessible.append(r)

    return accessible


def part1():
    rolls = get_rolls()
    print(len(get_accessibles(rolls)))


def part2():
    rolls = get_rolls()

    repeat = True
    tot = 0
    while repeat:
        acc = get_accessibles(rolls)
        if len(acc) > 0:
            tot += len(acc)
            [rolls.remove(a) for a in acc]
        else:
            break
    print(tot)


if __name__ == "__main__":
    part1()
    part2()
