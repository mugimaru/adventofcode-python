from functools import reduce
import operator


def part1(input: str) -> int:
    input = _parse_input(input)
    return sum([input[i][j] + 1 for i, j in _get_low_points(input)])


def part2(input: str) -> int:
    input = _parse_input(input)
    basins_size = [len(_find_basin(input, (i, j), set([(i, j)]))) for (i, j) in _get_low_points(input)]
    return reduce(operator.mul, sorted(basins_size, reverse=True)[0:3], 1)


def _find_basin(grid, p, acc):
    (i, j) = p
    cell = grid[i][j]

    def check_point(x, y):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] > cell and grid[x][y] != 9

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        newp = (i + di, j + dj)
        if check_point(newp[0], newp[1]):
            acc.add(newp)
            acc.union(_find_basin(grid, newp, acc))

    return acc


def _get_low_points(input: "list[list[int]]"):
    low_points = []
    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            is_low = (
                (i - 1 < 0 or input[i - 1][j] > cell)
                and (i + 1 >= len(input) or input[i + 1][j] > cell)
                and (j - 1 < 0 or input[i][j - 1] > cell)
                and (j + 1 >= len(row) or input[i][j + 1] > cell)
            )

            if is_low:
                low_points.append((i, j))
    return low_points


def _parse_input(input: str) -> "list[list[int]]":
    return [[int(cell) for cell in line] for line in input.splitlines()]
