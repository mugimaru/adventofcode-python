import sys


def part1(input: str) -> int:
    algo, bx, by, image = parse_input(input)
    image = enhance(algo, image, 2)
    return len(image)


def part2(input: str) -> int:
    algo, bx, by, image = parse_input(input)
    image = enhance(algo, image, 50)
    return len(image)


def parse_input(input: str):
    algo_, image_ = input.split("\n\n")
    algo = [char == "#" for char in algo_]

    image = set()
    image_lines = image_.splitlines()
    for y, line in enumerate(image_lines):
        for x, cell in enumerate(line):
            if cell == "#":
                image.add((x, y))

    return algo, (0, len(image_lines[0]) - 1), (0, len(image_lines) - 1), image


def enhance(algo, image, steps):
    visited = set()
    for step in range(steps):
        min_x, max_x, min_y, max_y = minmax(image)

        new_image = set()
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):

                if not step % 2:
                    visited.add((x, y))

                binary = []
                for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                    point = (x + dx, y + dy)
                    if step % 2 and point not in visited:
                        binary.append("1")
                    else:
                        binary.append("1" if point in image else "0")

                if algo[int("".join(binary), 2)]:
                    new_image.add((x, y))

        image = new_image
        if step % 2:
            visited = set()

    return image


def minmax(st):
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = 0, 0
    for (x, y) in st:
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

    return min_x, max_x, min_y, max_y
