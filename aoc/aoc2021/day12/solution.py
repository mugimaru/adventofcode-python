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
    routes = parse_input(input)
    paths = find_paths_p2("start", routes, [], None)
    return len(paths)


def find_paths_p2(start, routes, path, sc_visited_twice):
    path = list(path)
    path.append(start)
    paths = set([])
    for p in routes[start]:
        next_scvt = bool(sc_visited_twice)
        if p.upper() != p and p in path:
            if sc_visited_twice:
                continue
            else:
                next_scvt = True

        if p == "end":
            paths.add(",".join(path))
            continue
        if p == "start":
            continue

        paths = paths.union(find_paths_p2(p, routes, path, next_scvt))

    return paths


def parse_input(input: str) -> "dict[str, list[str]]":
    routes = defaultdict(set)

    for line in input.splitlines():
        a, b = line.split("-")
        routes[a].add(b)
        routes[b].add(a)
    return dict(routes)
