from collections import defaultdict


def part1(input: str) -> int:
    return _calculate_intersections(_parse_input(input), with_diagonal_lines=False)


def part2(input: str) -> None:
    return _calculate_intersections(_parse_input(input), with_diagonal_lines=True)

def _calculate_intersections(input: list[tuple[tuple[int, int], tuple[int, int]]], with_diagonal_lines=False) -> int:
    acc = defaultdict(int)

    for (x1, y1), (x2, y2) in input:
        if with_diagonal_lines or x1 == x2 or y1 == y2:
            while x1 != x2 or y1 != y2:
                acc[(x1, y1)] += 1
                if x1 != x2:
                    x1 += 1 if x1 < x2 else -1
                if y1 != y2:
                    y1 += 1 if y1 < y2 else -1
            acc[(x1, y1)] += 1

    intersections = 0
    for _, count in acc.items():
        if count > 1: intersections += 1

    return intersections


def _parse_input(input: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    return list(map(lambda line:
                    tuple(map(lambda coord:
                              tuple(map(lambda v: int(v), coord.split(','))), line.split(' -> '))), input.split('\n')))


if __name__ == "__main__":
    with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
        input = input_file.read()

    print(f'Part 1: {str(part1(input))}\nPart 2: {str(part2(input))}')
