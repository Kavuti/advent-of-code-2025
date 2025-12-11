from pprint import pprint
from functools import lru_cache
from dataclasses import dataclass
import heapq
from collections import defaultdict, deque

data = []

with open("src/i.txt") as file:
    data = file.read().splitlines()


@dataclass
class Machine:
    lights: list[int]
    diagram: list[int]
    buttons: list[tuple[int]]
    requirements: list[int]
    joltages: list[int]
    curr_min: int

    def __init__(self, line: str):
        split = line.split(" ")
        self.diagram = [0 if c == "." else 1 for c in split[0][1:-1]]
        self.lights = [0 for _ in self.diagram]
        self.buttons = sorted(
            [tuple([int(n) for n in s[1:-1].split(",")]) for s in split[1:-1]],
            key=lambda x: -len(x),
        )
        self.requirements = [int(n) for n in split[-1][1:-1].split(",")]
        self.joltages = [0 for _ in self.requirements]
        self.curr_min = len(self.buttons) * 1000000

    def press_lights(self, l, b):
        d = l.copy()
        for n in b:
            d[n] = 1 - d[n]
        return d

    def configure_joltage(self, j, b):
        d = j.copy()
        for n in b:
            d[n] += 1
        return d

    def steps_for_lights(self):
        min_steps = len(self.buttons) * 100000
        queue = deque()
        queue.append((self.lights.copy(), []))
        visited = set()
        while queue:
            situation, pressed = queue.popleft()
            if tuple(situation) in visited:
                continue
            visited.add(tuple(situation))
            if (
                all(v == w for v, w in zip(situation, self.diagram))
                and len(pressed) < min_steps
            ):
                min_steps = len(pressed)
            for button in self.buttons:
                if len(pressed) == 0 or button != pressed[-1]:
                    queue.append(
                        (self.press_lights(situation, button), pressed + [button])
                    )
        return min_steps

    def steps_for_joltages(self):
        min_steps = len(self.buttons) * 100000
        queue = deque()
        queue.append((self.joltages.copy(), []))
        visited = set()
        while queue:
            situation, pressed = queue.popleft()
            if tuple(situation) in visited:
                continue
            visited.add(tuple(situation))

            if (
                all(v == w for v, w in zip(situation, self.requirements))
                and len(pressed) < min_steps
            ):
                min_steps = len(pressed)
            for button in self.buttons:
                queue.append(
                    (self.configure_joltage(situation, button), pressed + [button])
                )
        return min_steps

    def steps_for_joltages_alt(self, situation, pressed):
        minimum = len(self.buttons) * 1000000
        if any([n > m for n, m in zip(situation, self.requirements)]):
            return minimum
        if all(v == w for v, w in zip(situation, self.requirements)):
            return len(pressed)

        # if len(pressed) < self.curr_min:
        for button in self.buttons:
            minimum = min(
                minimum,
                self.steps_for_joltages_alt(
                    self.configure_joltage(situation, button), pressed + [button]
                ),
            )
        return minimum

    def sub_j(self, s, b, m=1):
        d = s.copy()
        for n in b:
            d[n] -= m
        return d

    def steps_for_joltages_alt2(self):

        min_steps = len(self.buttons) * 100000
        queue = []
        heapq.heappush(queue, (0, self.requirements.copy(), []))
        visited = set()
        while queue:
            _, situation, pressed = heapq.heappop(queue)
            if tuple(situation) in visited:
                continue
            visited.add(tuple(situation))

            if (
                all(v == w for v, w in zip(situation, [0 for _ in self.requirements]))
                and len(pressed) < min_steps
            ):
                min_steps = len(pressed)
            if len(pressed) > 0:
                for i in range(10):
                    heapq.heappush(
                        queue,
                        (
                            -(len(pressed) + i + 1),
                            self.sub_j(situation, pressed[-1], i + 1),
                            pressed + [pressed[-1] for _ in range(i + 1)],
                        ),
                    )
            for button in self.buttons:
                heapq.heappush(
                    queue,
                    (
                        -(len(pressed) + 1),
                        self.sub_j(situation, button),
                        pressed + [button],
                    ),
                )
        return min_steps

    def steps_for_joltages_alt3(self):
        queue = deque([(self.requirements, [])])
        min_steps = len(self.requirements) * 100000
        while queue:
            situation, pressed = queue.popleft()
            if situation == [0 for _ in self.requirements]:
                min_steps = min(min_steps, len(pressed))

            if len(pressed) > 0:
                if any(situation[n] < 0 for n in pressed[-1]):
                    continue
                while all(situation[n] > 0 for n in pressed[-1]):
                    situation = self.sub_j(situation, pressed[-1])
                    pressed.append(pressed[-1])
                    for b in self.buttons:
                        if b not in pressed:
                            queue.append((self.sub_j(situation, b), pressed + [b]))
            else:
                for b in self.buttons:
                    queue.append((self.sub_j(situation, b), pressed + [b]))

        return min_steps

    def steps_for_joltages_alt4(self):
        queue = deque(
            [(self.sub_j(self.requirements, self.buttons[0]), [self.buttons[0]])]
        )
        min_steps = len(self.requirements) * 100000
        while queue:
            situation, pressed = queue.popleft()
            if any(situation[n] < 0 for n in pressed[-1]):
                continue
            if situation == [0 for _ in self.requirements]:
                min_steps = min(min_steps, len(pressed))

            while all(situation[n] > 0 for n in pressed[-1]):
                situation = self.sub_j(situation, pressed[-1])
                pressed.append(pressed[-1])

            if situation == [0 for _ in self.requirements]:
                min_steps = min(min_steps, len(pressed))

            for b in self.buttons:
                if b not in pressed:
                    queue.append(
                        (
                            self.sub_j(situation, b),
                            pressed + [b],
                        )
                    )

        return min_steps


def part1():
    tot = 0
    for line in data:
        f = Machine(line).steps_for_lights()
        tot += f
    print(tot)


# Totally not working
def part2():
    tot = 0
    for line in data:
        f = Machine(line).steps_for_joltages_alt4()
        # print(f)
        # f.steps_for_joltages_alt(f.joltages, [])
        # print(f.curr_min)
        tot += f
    print(tot)


if __name__ == "__main__":
    part1()
    part2()
