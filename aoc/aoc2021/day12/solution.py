from collections import defaultdict


def part1(input: str) -> int:
    routes = parse_input(input)
    paths = find_paths("start", routes, [])
    return len(paths)


def find_paths(start, routes, path):
    path = list(path)
    path.append(start)
    paths = set([])
    for p in routes[start]:
        if p.upper() != p and p in path:
            continue
        if p == "end":
            paths.add(",".join(path))
            continue
        paths = paths.union(find_paths(p, routes, path))

    return paths


def part2(input: str) -> int:
    pass


def parse_input(input: str) -> "dict[str, list[str]]":
    routes = defaultdict(set)

    for line in input.splitlines():
        a, b = line.split("-")
        routes[a].add(b)
        routes[b].add(a)
    return dict(routes)
