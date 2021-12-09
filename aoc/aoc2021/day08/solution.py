from itertools import permutations

DIGITS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

ALL_SEGMENTS = "abcdefg"


def part1(input: str) -> int:
    return sum(sum(1 for v in output if len(v) in [2, 3, 4, 7]) for (_signals, output) in _parse_input(input))


def part2(input: str) -> int:
    def translate(trans_map, pattern):
        translated = []
        for i in range(len(pattern)):
            translated.append(trans_map[pattern[i]])
        return sorted(translated)

    total_output = 0
    for (signals, outputs) in _parse_input(input):
        for permutation in permutations(ALL_SEGMENTS):
            trans_map = {}
            for i in range(len(permutation)):
                trans_map[permutation[i]] = ALL_SEGMENTS[i]

            translated_signals = [translate(trans_map, pattern) for pattern in signals]
            translated_outputs = [translate(trans_map, pattern) for pattern in outputs]
            if all("".join(pattern) in DIGITS for pattern in translated_signals):
                total_output += int("".join(str(DIGITS["".join(pattern)]) for pattern in translated_outputs))
                break

    return total_output


def _parse_input(input: str) -> list[int]:
    def parse_seq(input: str) -> list[str]:
        return list(map(list, input.split(" ")))

    parsed = []
    for line in input.splitlines():
        signals, output = line.split(" | ")
        parsed.append((parse_seq(signals), parse_seq(output)))

    return parsed
