def part1(input: str) -> int:
    grid, exit = parse_input(input)
    return find_best_path(grid, exit)


def part2(input: str) -> int:
    grid, exit = scale(*parse_input(input))
    return find_best_path(grid, exit)


def scale(grid, exit):
    new_grid = grid.copy()

    for (x, y), risk in grid.items():
        for i in range(5):
            for j in range(5):
                new_point = (x + i * (exit[0] + 1), y + j * (exit[1] + 1))
                new_risk = (risk + i + j) % 9
                new_risk = 9 if new_risk == 0 else new_risk
                new_grid[new_point] = new_risk

    new_exit = ((exit[0] + 1) * 5 - 1, (exit[1] + 1) * 5 - 1)
    return new_grid, new_exit


def find_best_path(grid: "dict[tuple[int, int], int]", exit: "tuple[int, int]") -> int:
    unvisited = set(grid.keys())
    routes = {(0, 0): 0}
    current_pos = (0, 0)

    while routes:
        x, y = current_pos
        risk = routes[current_pos]

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_point = (x + dx, y + dy)
            if next_point not in unvisited:
                continue

            current_risk = routes.get(next_point, None)
            new_risk = risk + grid[next_point]
            if not current_risk or new_risk < current_risk:
                routes[next_point] = new_risk

        unvisited.remove(current_pos)
        del routes[current_pos]

        lowest_risk = min(routes.values())
        for coords, risk in routes.items():
            if risk == lowest_risk:
                current_pos = coords
                break

        if current_pos == exit:
            return routes[exit]

    return None


def parse_input(input: str) -> "dict[tuple[int, int], int]":
    grid = {}
    lines = input.splitlines()
    for y, line in enumerate(lines):
        for x, risk_level in enumerate(line):
            grid[(x, y)] = int(risk_level)

    return grid, (len(lines[0]) - 1, len(lines) - 1)
