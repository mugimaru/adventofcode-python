import math
import re


class Board():

    def __init__(self, numbers: list[int]) -> None:
        self.numbers = {}
        self.size = int(math.sqrt(len(numbers)))
        self.rows = [0 for i in range(self.size)]
        self.cols = [0 for i in range(self.size)]
        self.marked = set([])

        for i, num in enumerate(numbers):
            self.numbers[num] = (i // self.size, i % self.size)

    def mark_number(self, num: int) -> bool:
        if not num in self.numbers:
            return False

        (row, col) = self.numbers[num]
        self.rows[row] += 1
        self.cols[col] += 1
        self.marked.add(num)

        return self.rows[row] >= self.size or self.cols[col] >= self.size

    def score(self, num: int) -> int:
        sum = 0
        for item in self.numbers:
            if not item in self.marked:
                sum += item

        return sum * num


def part1(input: str):
    nums, boards = _parse_input(input)
    return _find_winners_score(nums, boards)


def part2(input):
    nums, boards = _parse_input(input)
    return _find_loosers_score(nums, boards, [])


def _find_winners_score(nums, boards) -> int:
    for num in nums:
        for board in boards:
            if board.mark_number(num):
                return board.score(num)


def _find_loosers_score(nums, boards, winners) -> int:
    if len(boards) == 0:
        (board, num) = winners[-1]
        return board.score(num)

    filtered_boards = []
    for board in boards:
        if board.mark_number(nums[0]):
            winners.append((board, nums[0]))
        else:
            filtered_boards.append(board)

    return _find_loosers_score(nums[1:], filtered_boards, winners)


def _parse_input(input: str) -> tuple[list[int], list[Board]]:
    nums, *boards = input.split('\n\n')
    nums = [int(num) for num in nums.split(",")]
    boards = list(map(lambda board: Board([int(num)
                                           for num in re.split("\D+", board.strip())]), boards))

    return nums, boards