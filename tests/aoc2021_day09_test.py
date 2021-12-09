from aoc.aoc2021.day09 import solution

TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def test_part1():
    assert solution.part1(TEST_INPUT) == 15


def test_part2():
    assert solution.part2(TEST_INPUT) is None
