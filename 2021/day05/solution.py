from collections import defaultdict


def part1(input: str) -> int:
    acc = defaultdict(int)

    for (x1, y1), (x2, y2) in _parse_input(input):
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                acc[(x1, y)] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                acc[(x, y1)] += 1

    intersections = 0
    for (x, y), count in acc.items():
        if count > 1:
            intersections += 1
    return intersections


def part2(input: str) -> None:
    return None


def _parse_input(input: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return list(map(lambda line:
                    tuple(map(lambda coord:
                              tuple(map(lambda v: int(v), coord.split(','))), line.split(' -> '))), input.split('\n')))


if __name__ == "__main__":
    with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
        input = input_file.read()

    print(f'Part 1: {str(part1(input))}\nPart 2: {str(part2(input))}')
