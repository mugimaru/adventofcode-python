from aoc2021.day06 import solution

TEST_INPUT = "3,4,3,1,2"

def test_part1():
    assert solution.part1(TEST_INPUT, days=18) == 26
    assert solution.part1(TEST_INPUT, days=80) == 5934

def test_part2():
    assert solution.part2(TEST_INPUT) == 26984457539

