from aoc.aoc2021.day01 import solution

TEST_INPUT = """199
200
208
210
200
207
240
269
260
263"""

def test_part1():
    assert solution.part1(TEST_INPUT) == 7

def test_part2():
    assert solution.part2(TEST_INPUT) == 5
