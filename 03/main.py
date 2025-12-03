import re
import heapq
from functools import lru_cache
from itertools import combinations

data = []

with open("input.txt") as file:
    data = file.read().splitlines()

@lru_cache(maxsize=None)
def explore(n, l, last=None):
    if len(str(n)) == 1:
        return max([int(c) for c in str(n)])
    if l == 1:
        return max([int(c) for c in str(n)])
    else:
        v = max(
            int(str(n)[0] + str(explore(str(n)[1:], l - 1, str(n)[0]))),
            int(explore(str(n)[1:], l, last)),
        )
        return v

def part1():
    tot = 0
    for i, line in enumerate(data):
        r = explore(int(line), 2)
        tot += r
    print(tot)


def part2():
    tot = 0
    for i, line in enumerate(data):
        r = explore(int(line), 12)
        tot += r
    print(tot)


if __name__ == "__main__":
    part1()
    part2()
