from collections import defaultdict


def part1(input: str) -> int:
    return solve(input, 10)


def part2(input: str) -> int:
    pass


def solve(input, steps):
    template, insertions = parse_input(input)
    for _ in range(steps):
        template = iterate(template, insertions)

    stats = defaultdict(int)
    for char in template:
        stats[char] += 1

    mc = max(stats, key=stats.get)
    lc = min(stats, key=stats.get)

    return stats[mc] - stats[lc]


def iterate(template: str, insertions: "dict[str, str]") -> str:
    new_template = template[0]
    for i in range(len(template) - 1):
        seq = template[i:i + 2]
        ins = insertions.get(seq)
        if ins is not None:
            new_template += ins + template[i + 1]
        else:
            template[i + 1]

    return new_template


def parse_input(input: str):
    template, insertions_ = input.split("\n\n")
    insertions = {}
    for line in insertions_.splitlines():
        k, v = line.split(" -> ")
        insertions[k] = v
    return template, insertions
