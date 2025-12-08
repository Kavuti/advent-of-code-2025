from pprint import pprint
from collections import defaultdict
from functools import lru_cache
from os import system

import math

data = []

with open("input.txt") as file:
    data = file.read().splitlines()


def euclidean_dist(x, y):
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2)


def points_id(x, y):
    return tuple(sorted([x, y]))


points = []
for line in data:
    points.append(tuple(int(x) for x in line.split(",")))

dists = {}
for p in points:
    for p2 in points:
        if p != p2 and points_id(p, p2) not in dists:
            dists[points_id(p, p2)] = euclidean_dist(p, p2)

sorted_keys = sorted(dists, key=dists.get)


def calc(points, sorted_keys, num):
    g_dict = {p: i for i, p in enumerate(points)}
    final_k = None
    for k in sorted_keys[:num]:
        o0, o1 = g_dict[k[0]], g_dict[k[1]]
        m = min(g_dict[k[0]], g_dict[k[1]])
        g_dict[k[0]] = m
        g_dict[k[1]] = m

        if m != o0:
            for kk in g_dict.keys():
                if g_dict[kk] == o0:
                    g_dict[kk] = m
        elif m != o1:
            for kk in g_dict.keys():
                if g_dict[kk] == o1:
                    g_dict[kk] = m
        if len(set(g_dict.values())) == 1:
            final_k = k
            break
    inv = defaultdict(list)
    for k, v in g_dict.items():
        inv[v].append(k)

    skeys = sorted(inv, key=lambda x: len(inv.get(x)), reverse=True)[:3]
    tot = 1
    for s in skeys:
        tot *= len(inv[s])

    return tot, final_k


def part1():
    m, _ = calc(points, sorted_keys, 1001)
    print(m)


def part2():
    _, equals = calc(points, sorted_keys, len(sorted_keys))
    print(equals[0][0] * equals[1][0])


if __name__ == "__main__":
    part1()
    part2()
