from aoc.aoc2021.day12 import solution


def test_part1():

    assert (
        solution.part1(
            """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
        )
        == 10
    )

    assert (
        solution.part1(
            """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
        )
        == 19
    )

    assert (
        solution.part1(
            """fs-end
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
        )
        == 226
    )


def test_part2():
    pass
