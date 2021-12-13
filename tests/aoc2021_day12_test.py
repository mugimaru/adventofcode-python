from aoc.aoc2021.day12 import solution

TI_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TI_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

TI_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def test_part1():
    assert solution.part1(TI_1) == 10
    assert solution.part1(TI_2) == 19
    assert solution.part1(TI_3) == 226


def test_part2():
    assert solution.part2(TI_1) == 36
    assert solution.part2(TI_2) == 103
    assert solution.part2(TI_3) == 3509
