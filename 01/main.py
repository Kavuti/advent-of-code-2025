from collections import deque, defaultdict
import heapq
from functools import lru_cache
from itertools import combinations_with_replacement

data = []

with open("input.txt") as file:
    data = file.read().splitlines()


def left(curr, n):
    return (curr - n) % 100, (n // 100) + int((n % 100) > curr if curr != 0 else 0)


def right(curr, n):
    return (curr + n) % 100, (
        (n // 100) + int((n % 100) > (100 - curr) if (100 - curr) != 0 else 0)
    )


def main():
    pos = 50

    total_1 = 0
    total_2 = 0
    for line in data:
        if line[0] == "L":
            pos, passed_zero = left(pos, int(line[1:]))
        elif line[0] == "R":
            pos, passed_zero = right(pos, int(line[1:]))
        total_2 += passed_zero
        if pos == 0:
            total_1 += 1
            total_2 += 1

    print(total_1)
    print(total_2)


if __name__ == "__main__":
    main()
