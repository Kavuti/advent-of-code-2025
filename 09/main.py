from pprint import pprint
from collections import defaultdict, deque
from functools import lru_cache
from os import system

import math

data = []

with open("src/i.txt") as file:
    data = file.read().splitlines()


def id(x, y):
    return tuple(sorted([x, y]))


points = []
for line in data:
    ls = line.split(",")
    points.append((int(ls[0]), int(ls[1])))

max_x = max(p[0] for p in points)


def part1():
    quads = {}
    for p1 in points:
        for p2 in points:
            if p1 != p2 and id(p1, p2) not in quads:
                quads[id(p1, p2)] = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
    print(max(quads.values()))


def fill_inside(p):
    bx = sorted(p, key=lambda x: (x[0], x[1]))
    by = sorted(p, key=lambda x: (x[1], x[0]))
    all_borders = set()
    queue = deque([bx[0]])
    visited = set()
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        ix = bx.index(curr)
        iy = by.index(curr)

        xr = bx[(ix + 1) % len(bx)]
        xl = bx[(ix - 1) % len(bx)]

        if xr[0] == curr[0]:
            all_borders.add(curr)
            # for ixi in range(min(xr[1], curr[1]), max(xr[1], curr[1])):
            # all_borders.add((curr[0], ixi))
            queue.append(xr)
        if xl[0] == curr[0]:
            all_borders.add(curr)
            # for ixi in range(min(xl[1], curr[1]), max(xl[1], curr[1])):
            # all_borders.add((curr[0], ixi))
            queue.append(xl)

        yr = by[(iy + 1) % len(by)]
        yl = by[(iy - 1) % len(by)]
        if yr[1] == curr[1]:
            all_borders.add(curr)
            for iyi in range(min(yr[0], curr[0]), max(yr[0], curr[0])):
                all_borders.add((iyi, curr[1]))
                # pass
            queue.append(yr)
        if yl[1] == curr[1]:
            all_borders.add(curr)
            for iyi in range(min(yl[0], curr[0]), max(yl[0], curr[0])):
                all_borders.add((iyi, curr[1]))
                # pass
            queue.append(yl)

    return all_borders


def part2():
    all_borders = sorted(fill_inside(points))
    print(all_borders)
    # input()
    # all_tiles = sorted(fill_inside(all_borders))

    borders_idx = defaultdict(list)
    for b in all_borders:
        borders_idx[b[0]].append(b[1])
    print("indexed")

    for k in borders_idx.keys():
        borders_idx[k].sort(reverse=True)
    print("sorted")

    print(borders_idx)

    quads = {}
    for p1 in points:
        for p2 in points:
            if p1 != p2 and id(p1, p2) not in quads:
                # print(p1, p2)
                # print((p1[0], p2[1]), (p2[0], p1[1]))
                # input()
                valid = True
                if not (p1[0], p2[1]) in all_borders:
                    count = 0
                    for c in borders_idx[p1[0]]:
                        if c < p2[1]:
                            break
                        count += 1
                    if count % 2 == 0:
                        valid = False

                if not (p2[0], p1[1]) in all_borders:
                    count = 0
                    for c in borders_idx[p2[0]]:
                        if c < p1[1]:
                            break
                        count += 1
                    if count % 2 == 0:
                        valid = False

                if valid:
                    quads[id(p1, p2)] = (abs(p1[0] - p2[0]) + 1) * (
                        abs(p1[1] - p2[1]) + 1
                    )
                    print(p1, p2, quads[id(p1, p2)])
    print(max(quads.values()))


if __name__ == "__main__":
    part1()
    part2()
