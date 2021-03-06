from aoc.aoc2021.day15 import solution

TEST_INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_part1():
    assert solution.part1(TEST_INPUT) == 40


def test_part2():
    assert solution.part2(TEST_INPUT) == 315
