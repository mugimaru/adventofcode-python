from aoc.aoc2021.day05 import solution

TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_part1():
    assert solution.part1(TEST_INPUT) == 5


def test_part2():
    assert solution.part2(TEST_INPUT) == 12
