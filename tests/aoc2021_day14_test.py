from aoc.aoc2021.day14 import solution

TEST_INPUT = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_part1():
    assert solution.part1(TEST_INPUT) == 1588


def test_part2():
    assert solution.part2(TEST_INPUT) == 2188189693529
