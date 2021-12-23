from aoc.aoc2021.day17 import solution

TEST_INPUT = "target area: x=20..30, y=-10..-5"


def test_part1():
    assert solution.part1(TEST_INPUT) == 45


def test_part2():
    assert solution.part2(TEST_INPUT) == 112
