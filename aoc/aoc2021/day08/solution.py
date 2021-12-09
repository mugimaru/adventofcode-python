def part1(input: str) -> int:
    return sum(sum(1 for v in output if len(v) in [2, 3, 4, 7]) for (_signals, output) in _parse_input(input))


def part2(input: str) -> int:
    pass


def _parse_input(input: str) -> list[int]:
    def parse_seq(input: str) -> list[str]:
        return list(map(list, input.split(" ")))

    parsed = []
    for line in input.splitlines():
        signals, output = line.split(" | ")
        parsed.append((parse_seq(signals), parse_seq(output)))

    return parsed
