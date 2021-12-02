def part1(input):
    input = _parse_input(input)
    current = None
    counter = 0

    for v in input:
        if current != None and v > current:
            counter += 1
        current = v

    return counter

def part2(input):
    input = _parse_input(input)
    i = 1
    counter = 0
    curr = input[0] + input[1] + input[2]
    while i < len(input) - 2:
        sum = input[i] + input[i + 1] + input[i + 2]
        if sum > curr:
            counter += 1
        curr = sum
        i += 1

    return counter

def _parse_input(input):
    return list(map(lambda line: int(line), input))

if __name__ == "__main__":
    with open((__file__.rstrip("solution.py")+"input.txt"), 'r') as input_file:
        input = [int(line) for line in input_file.read().splitlines()]

    print(f'Part 1: {str(part1(input))}\nPart 2: {str(part2(input))}')