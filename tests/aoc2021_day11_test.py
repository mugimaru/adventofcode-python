from aoc.aoc2021.day11 import solution

TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_part1():
    assert solution.part1(TEST_INPUT) == 1656


def test_part2():
    assert solution.part2(TEST_INPUT) == 195
