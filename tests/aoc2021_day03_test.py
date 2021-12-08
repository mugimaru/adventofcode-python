from aoc2021.day03 import solution

TEST_INPUT = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010'
]

def test_part1():
    assert solution.part1(TEST_INPUT) == 198

def test_part2():
    assert solution.part2(TEST_INPUT) == 230

