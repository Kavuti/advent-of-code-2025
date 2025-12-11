from functools import lru_cache
data = []

with open("input.txt") as file:
    data = file.read().splitlines()

graph = {}
for line in data:
    k, v = line.split(": ")
    graph[k] = v.split(" ")


def reaches_out(n, visited=["you"]):
    if n == "out":
        return 1
    else:
        c = 0
        for v in graph[n]:
            if v not in visited:
                c += reaches_out(v, visited + [v])
        return c


def get_valid_paths(start):
    visited = set()

    @lru_cache(maxsize=None)
    def reaches_new(n, got_dac=False, got_fft=False):
        if n == "out":
            return 1 if got_dac and got_fft else 0
        else:
            c = 0
            visited.add(n)
            for v in graph[n]:
                if v not in visited:
                    c += reaches_new(v, "dac" in visited, "fft" in visited)
            visited.remove(n)
            return c

    return reaches_new(start)


def part1():
    v = reaches_out("you")
    print(v)


def part2():
    v = get_valid_paths("svr")
    print(v)


if __name__ == "__main__":
    part1()
    part2()
