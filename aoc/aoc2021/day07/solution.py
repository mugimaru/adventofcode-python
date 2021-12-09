def part1(input: str) -> int:
    return _solve(input, lambda c1, c2: abs(c1 - c2))


def part2(input: str) -> int:
    return _solve(input, lambda c1, c2: abs(c1 - c2) * (abs(c1 - c2) + 1) // 2)


def _solve(input: str, distance_fun) -> int:
    input = _parse_input(input)
    return min(
        map(
            lambda c1: sum(map(lambda c2: distance_fun(min(c1, c2), max(c1, c2)), input)),
            range(min(input), max(input) + 1),
        )
    )


def _parse_input(input: str) -> list[int]:
    return [int(num) for num in input.split(",")]
