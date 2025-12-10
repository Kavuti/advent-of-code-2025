from collections import defaultdict, deque
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
            for ixi in range(min(xr[1], curr[1]), max(xr[1], curr[1])):
                all_borders.add((curr[0], ixi))
            queue.append(xr)
        if xl[0] == curr[0]:
            all_borders.add(curr)
            for ixi in range(min(xl[1], curr[1]), max(xl[1], curr[1])):
                all_borders.add((curr[0], ixi))
            queue.append(xl)

        yr = by[(iy + 1) % len(by)]
        yl = by[(iy - 1) % len(by)]
        if yr[1] == curr[1]:
            all_borders.add(curr)
            for iyi in range(min(yr[0], curr[0]), max(yr[0], curr[0])):
                all_borders.add((iyi, curr[1]))
            queue.append(yr)
        if yl[1] == curr[1]:
            all_borders.add(curr)
            for iyi in range(min(yl[0], curr[0]), max(yl[0], curr[0])):
                all_borders.add((iyi, curr[1]))
            queue.append(yl)

    return all_borders


# Totally not working
def part2():
    all_borders = set(sorted(fill_inside(points)))

    borders_idx = defaultdict(list)
    for b in all_borders:
        borders_idx[b[0]].append(b[1])

    for k in borders_idx.keys():
        borders_idx[k].sort(reverse=True)

    conteggio = 0
    quads = {}
    invalids = set()
    for p1 in points:
        for p2 in points:
            conteggio += 1
            print(conteggio)
            if p1 != p2 and id(p1, p2) not in quads and id(p2, p1) not in invalids:
                valid = True
                if not (p1[0], p2[1]) in all_borders:
                    count = 0
                    for pos, c in enumerate(borders_idx[p1[0]]):
                        if c < p2[1]:
                            break
                        if (
                            borders_idx[p1[0]][len(borders_idx[p1[0]]) - pos - 2]
                            != c + 1
                            or borders_idx[p1[0]][len(borders_idx[p1[0]]) - pos]
                            != c - 1
                        ):
                            count += 1
                    if count % 2 == 0:
                        valid = False
                    else:
                        all_borders.add((p1[0], p2[1]))

                if not (p2[0], p1[1]) in all_borders and valid:
                    count = 0
                    for pos, c in enumerate(borders_idx[p2[0]]):
                        if c < p1[1]:
                            break
                        if (
                            borders_idx[p2[0]][len(borders_idx[p2[0]]) - pos - 2]
                            != c + 1
                            or borders_idx[p2[0]][len(borders_idx[p2[0]]) - pos]
                            != c - 1
                        ):
                            count += 1
                    if count % 2 == 0:
                        valid = False
                    else:
                        all_borders.add((p2[0], p1[1]))

                if valid:
                    quads[id(p1, p2)] = (abs(p1[0] - p2[0]) + 1) * (
                        abs(p1[1] - p2[1]) + 1
                    )
                else:
                    invalids.add(id(p1, p2))

    print(max(quads.values()))


def part2_alt():
    from shapely import Polygon, box

    polygon = Polygon(points)
    maxx = 0
    for p1 in points:
        for p2 in points:
            if p1 != p2 and polygon.contains(box(p1[0], p1[1], p2[0], p2[1])):
                maxx = max(maxx, (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1))
    print(maxx)


if __name__ == "__main__":
    part1()
    part2_alt()
