from functools import reduce

cto = {">": "<", "}": "{", ")": "(", "]": "["}
otc = {v: k for k, v in cto.items()}
sc_scores = {">": 25137, "}": 1197, ")": 3, "]": 57}
ac_scores = {">": 4, "}": 3, ")": 1, "]": 2}


def part1(input: str) -> int:
    score = 0
    for line in input.splitlines():
        _res, s, _stack = is_corrupted(line)
        score += s

    return score


def part2(input: str) -> int:
    scores = []
    for line in input.splitlines():
        corrupted, _score, stack = is_corrupted(line)
        if not corrupted:
            stack.reverse()
            score = reduce(lambda acc, char: (acc * 5) + ac_scores[otc[char]], stack, 0)
            scores.append(score)

    scores.sort()
    return scores[len(scores) // 2]


def is_corrupted(line) -> 'tuple[bool, int, list[str]]':
    stack = []
    for char in line:
        if char not in cto.keys():
            stack.append(char)
        else:
            op = stack.pop()
            if op != cto[char]:
                return (True, sc_scores[char], stack)
    return (False, 0, stack)
