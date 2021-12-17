import re
import sys
from functools import reduce


def part1(input: str) -> int:
    grid, instructions = parse_input(input)
    axis, n = instructions[0]
    return len(set(fold(p, axis, n) for p in grid))


def part2(input: str) -> str:
    grid, instructions = parse_input(input)

    def fold_grid(grid, instruction):
        return set(fold(p, instruction[0], instruction[1]) for p in grid)

    grid = reduce(fold_grid, instructions, grid)

    max_x, max_y, min_x, min_y = 0, 0, sys.maxsize, sys.maxsize
    for (x, y) in grid:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

    out = "\n\n"
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):

            out += "#" if (x, y) in grid else " "
        out += "\n"

    return out


def fold(point, axis, n):
    x, y = point
    if axis == "x":
        new_x = n + (n - x) if x > n else x
        return (new_x, y)
    else:
        new_y = n + (n - y) if y > n else y
        return (x, new_y)


def parse_input(input: str):
    grid = set()
    instructions = []
    grid_, instructions_ = input.split("\n\n")

    for line in grid_.splitlines():
        x, y = line.strip().split(",")
        grid.add((int(x), int(y)))

    for line in instructions_.splitlines():
        md = re.match(r"fold along (y|x)=(\d+)", line)
        instructions.append((md[1], int(md[2])))

    return grid, instructions
