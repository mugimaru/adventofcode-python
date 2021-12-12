import queue
from itertools import product


def part1(input: str) -> int:
    acc = 0
    grid = parse_input(input)
    for x in range(100):
        acc += simulate_step(grid)
    return acc


def part2(input: str) -> int:
    grid = parse_input(input)
    cnt = len(grid[0]) * len(grid)
    step = 0
    while True:
        step += 1
        if simulate_step(grid) == cnt:
            break
    return step


def simulate_step(grid: "list[list[int]]") -> int:
    flashed = set([])
    with_max_energy = queue.SimpleQueue()

    def charge(i, j):
        if i < 0 or j < 0 or i >= len(grid[0]) or j >= len(grid):
            return

        grid[i][j] += 1
        if grid[i][j] == 10:
            with_max_energy.put((i, j))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            charge(i, j)

    while not with_max_energy.empty():
        i, j = with_max_energy.get()
        flashed.add((i, j))
        for di, dj in product([1, 0, -1], [1, 0, -1]):
            if di == 0 and dj == 0:
                pass
            charge(i + di, j + dj)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                grid[i][j] = 0
    return len(flashed)


def parse_input(input: str) -> "list[list[int]]":
    return [[int(o) for o in list(line)] for line in input.splitlines()]
