def part1(input: str, days=80) -> int:
    return sum(_simulate(_parse_input(input), days))


def part2(input: str) -> int:
    return part1(input, days=256)


def _simulate(input: list[int], days: int) -> list[int]:
    next_gen = input[1:]
    next_gen[6] += input[0]
    next_gen.append(input[0])

    if days > 1:
        return _simulate(next_gen, days - 1)
    else:
        return next_gen


def _parse_input(input: str) -> list[int]:
    acc = [0 for _ in range(0, 9)]
    for item in input.split(","):
        acc[int(item)] += 1

    return acc
