from aoc.aoc2021.day07 import solution

TEST_INPUT = "16,1,2,0,4,2,7,1,2,14"


def test_part1():
    assert solution.part1(TEST_INPUT) == 37


def test_part2():
    assert solution.part2(TEST_INPUT) == 168
