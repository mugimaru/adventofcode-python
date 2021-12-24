import re


def part1(input):
    def limited_range(minv, maxv):
        return range(max(minv, -50), min(maxv, 50) + 1)

    cubes = set()
    for (cmd, (min_x, max_x, min_y, max_y, min_z, max_z)) in parse_input(input):
        for x in limited_range(min_x, max_x):
            for y in limited_range(min_y, max_y):
                for z in limited_range(min_z, max_z):
                    (cubes.add if cmd else cubes.discard)((x, y, z))

    return len(cubes)


def part2(input):
    pass


def parse_input(input):
    data = []
    for line in input.splitlines():
        md = re.match(r"\w+ x=([\-0-9]+)\.\.([\-0-9]+),y=([\-0-9]+)\.\.([\-0-9]+),z=([\-0-9]+)\.\.([\-0-9]+)", line)

        data.append((line[0:2] == "on", tuple(map(int, md.groups()))))
    return data
