from typing import Match


def part1(input):
  input = _parse_input(input)

  x = 0
  depth = 0

  for (dir, value) in input:
    match dir:
        case "forward":
            x += value
        case "up":
          depth -= value
        case "down":
          depth += value

  return x * depth

def part2(input):
  input = _parse_input(input)

  aim = 0
  x = 0
  depth = 0

  for (dir, value) in input:
    match dir:
        case "forward":
            x += value
            depth += aim * value
        case "up":
          aim -= value
        case "down":
          aim += value

  return x * depth

def _parse_input(input):
  parsed = []

  for line in input.splitlines():
    cmd, value = line.split(" ")
    parsed.append((cmd, int(value)))

  return parsed