import re
from math import floor, ceil
from itertools import permutations


def part1(input: str) -> int:
    numbers = parse_input(input)
    result = []
    for number in numbers:
        result = add(result, number)
    result = eval("".join(map(str, result)))

    return magnitude(result)


def part2(input: str) -> int:
    numbers = parse_input(input)
    return max(
        magnitude(eval("".join(map(str, add(combination[0], combination[1])))))
        for combination in permutations(numbers, 2)
    )


def magnitude(number):
    mag = 0
    left, right = number
    left = left if isinstance(left, int) else magnitude(left)
    right = right if isinstance(right, int) else magnitude(right)
    mag += 3 * left + 2 * right
    return mag


def reduce(number):
    depth = 0
    for i, el in enumerate(number):
        if isinstance(el, str):
            if el == "[":
                depth += 1
            elif el == "]":
                depth -= 1
            if depth > 4:
                number = explode(number, i)
                number = reduce(number)
                break

    for i, el in enumerate(number):
        if isinstance(el, int) and el >= 10:
            number = reduce(split(number, i))
            break

    return number


def explode(number, i):
    def first_regular_num(number):
        for i, el in enumerate(number):
            if isinstance(el, int):
                return i, el

    n = [number[i + 1], number[i + 3]]
    if left := first_regular_num(number[i::-1]):
        number[i - left[0]] += n[0]
    if right := first_regular_num(number[i + 4 :]):
        number[i + 4 + right[0]] += n[1]
    number[i : i + 5] = [0]
    return number


def split(number, i):
    number[i : i + 1] = ["[", floor(number[i] / 2), ",", ceil(number[i] / 2), "]"]
    return number


def add(left, right):
    return reduce(["[", *left, ",", *right, "]"] if left else right)


def parse_input(input: str):
    return [
        [int(char) if char.isnumeric() else char for char in re.findall(r"(\[|]|,|[0-9]+)", line)]
        for line in input.splitlines()
    ]
