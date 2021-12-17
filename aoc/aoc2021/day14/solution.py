from collections import defaultdict
from functools import reduce


def part1(input: str) -> int:
    return solve(input, 10)


def part2(input: str) -> int:
    return solve(input, 40)


def solve(input, steps):
    template, insertions, last_letter = parse_input(input)
    template = reduce(lambda template, _: iterate(template, insertions), range(steps), template)
    return score(template, last_letter)


def score(template, last_letter):
    stats = defaultdict(int)
    for pair, cnt in template.items():
        stats[pair[0]] += cnt
    stats[last_letter] += 1

    mc = max(stats, key=stats.get)
    lc = min(stats, key=stats.get)
    return stats[mc] - stats[lc]


def iterate(template: "dict[str, int]", insertions: "dict[str, list[str]]") -> str:
    new_template = dict()
    for pair, cnt in template.items():
        for p in insertions.get(pair, []):
            new_template[p] = new_template.get(p, 0) + cnt

    return new_template


def parse_input(input: str):
    template_, insertions_ = input.split("\n\n")

    template = defaultdict(int)
    for i in range(len(template_) - 1):
        template[template_[i : i + 2]] += 1

    insertions = {}
    for line in insertions_.splitlines():
        k, v = line.split(" -> ")
        insertions[k] = [k[0] + v, v + k[1]]

    return template, insertions, template_[-1]
