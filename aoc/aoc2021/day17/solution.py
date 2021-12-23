import re


def part1(input: str) -> int:
    (x1, x2), (y1, y2) = parse_input(input)
    return max(check_hits_target(vx, vy, (x1, x2), (y1, y2))[1] for vx in range(x2 + 1) for vy in range(y1, -y1))


def part2(input: str) -> int:
    (x1, x2), (y1, y2) = parse_input(input)
    return sum(check_hits_target(vx, vy, (x1, x2), (y1, y2))[0] for vx in range(x2 + 1) for vy in range(y1, -y1))


def check_hits_target(vx, vy, ta_x, ta_y):
    x, y = (0, 0)
    max_y = 0
    while True:
        x += vx
        y += vy
        if y > max_y:
            max_y = y

        if x >= ta_x[0] and x <= ta_x[1] and y >= ta_y[0] and y <= ta_y[1]:
            return True, max_y

        if vx != 0:
            vx -= 1 if vx > 0 else -1

        vy -= 1

        if y <= ta_y[0] or x >= ta_x[1]:
            return False, 0


def parse_input(input: str) -> "tuple[tuple[int, int], tuple[int, int]]":
    md = re.match(r"target area: x=([\-0-9]+)..([\-0-9]+), y=([\-0-9]+)..([\-0-9]+)", input.strip())
    return (int(md[1]), int(md[2])), (int(md[3]), int(md[4]))
