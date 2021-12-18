from functools import reduce


class Packet:
    def __init__(self, version, type_id, subpackets=[], literal_value=None) -> None:
        self.version = version
        self.type_id = type_id
        self.subpackets = subpackets
        self.literal_value = literal_value

    def sum_versions(self):
        return self.version + sum(sp.sum_versions() for sp in self.subpackets)

    def value(self):
        match self.type_id:
            case 4:
                return self.literal_value
            case 0:  # sum
                return sum(sp.value() for sp in self.subpackets)
            case 1:  # product
                return reduce(lambda a, b: a * b, [sp.value() for sp in self.subpackets], 1)
            case 2:  # min
                return min(sp.value() for sp in self.subpackets)
            case 3:  # max
                return max(sp.value() for sp in self.subpackets)
            case 5:  # gt
                return 1 if self.subpackets[0].value() > self.subpackets[1].value() else 0
            case 6:  # lt
                return 1 if self.subpackets[0].value() < self.subpackets[1].value() else 0
            case 7:  # eq
                return 1 if self.subpackets[0].value() == self.subpackets[1].value() else 0


def part1(input: str) -> int:
    _, packet = parse_packet(hex_to_bin(input), 0)
    return packet.sum_versions()


def part2(input: str) -> int:
    _, packet = parse_packet(hex_to_bin(input), 0)
    return packet.value()


def parse_packet(input, pos):
    pos, version, type_id = parse_header(input, pos)

    if type_id == 4:
        pos, literal_value = parse_literal(input, pos)
        return pos, Packet(version, type_id, literal_value=literal_value)
    else:
        subpackets = []
        length_type_id = input[pos]
        pos += 1
        match length_type_id:
            case "0":
                num_bits_subpackets = int(input[pos : pos + 15], 2)
                pos += 15
                end_pos = pos + num_bits_subpackets
                while pos != end_pos:
                    pos, sp = parse_packet(input, pos)
                    subpackets.append(sp)
            case "1":
                num_subpackets = int(input[pos : pos + 11], 2)
                pos += 11
                for _ in range(num_subpackets):
                    pos, sp = parse_packet(input, pos)
                    subpackets.append(sp)

        return pos, Packet(version, type_id, subpackets=subpackets)


def parse_header(input, pos) -> "tuple[int, int]":
    version = input[pos : pos + 3]
    type_id = input[pos + 3 : pos + 6]
    return pos + 6, int(version, 2), int(type_id, 2)


def parse_literal(input, pos) -> "tuple[int, str]":
    last_group = False
    value = []
    while not last_group:
        last_group = input[pos] == "0"
        value.append(input[pos + 1 : pos + 5])
        pos += 5

    return pos, int("".join(value), 2)


h2b = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_bin(hex):
    return "".join(h2b[char] for char in hex)
