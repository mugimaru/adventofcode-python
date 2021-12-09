def part1(input: str) -> int:
    input = _parse_input(input)
    risk_level = 0
    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            is_low = (
                (i - 1 < 0 or input[i - 1][j] > cell)
                and (i + 1 >= len(input) or input[i + 1][j] > cell)
                and (j - 1 < 0 or input[i][j - 1] > cell)
                and (j + 1 >= len(row) or input[i][j + 1] > cell)
            )

            if is_low:
                risk_level += cell + 1
    return risk_level


def part2(input: str) -> int:
    pass


def _parse_input(input: str) -> "list[list[int]]":
    return [[int(cell) for cell in line] for line in input.splitlines()]
