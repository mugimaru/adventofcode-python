from aoc.aoc2021.day16 import solution


def test_part1():
    assert solution.part1("620080001611562C8802118E34") == 12
    assert solution.part1("D2FE28") == 6
    assert solution.part1("EE00D40C823060") == 14
    assert solution.part1("8A004A801A8002F478") == 16
    assert solution.part1("C0015000016115A2E0802F182340") == 23
    assert solution.part1("A0016C880162017C3686B18A3D4780") == 31


def test_part2():
    assert solution.part2("C200B40A82") == 3
    assert solution.part2("04005AC33890") == 54
    assert solution.part2("880086C3E88112") == 7
    assert solution.part2("CE00C43D881120") == 9
    assert solution.part2("D8005AC2A8F0") == 1
    assert solution.part2("F600BC2D8F") == 0
    assert solution.part2("9C005AC2F8F0") == 0
    assert solution.part2("9C0141080250320F1802104A08") == 1
