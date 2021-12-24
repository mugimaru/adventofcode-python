def part1(input: str) -> int:
    class DeterministicDie:
        def __init__(self) -> None:
            self.rolls = 0

        def roll(self):
            self.rolls += 1
            return ((self.rolls - 1) % 100) + 1

    def play(positions, die):
        scores = [0, 0]
        while True:
            for i in range(2):
                roll = sum([die.roll() for _ in range(3)])
                positions[i] = ((positions[i] + roll - 1) % 10) + 1
                scores[i] += positions[i]

                if scores[i] >= 1000:
                    return scores

    positions = parse_input(input)
    die = DeterministicDie()
    scores = play(positions, die)

    return die.rolls * min(scores)


def part2(input: str) -> int:
    cache = {}

    def play(p1_pos, p1_score, p2_pos, p2_score):
        if p1_score >= 21:
            return (1, 0)
        if p2_score >= 21:
            return (0, 1)

        state = (p1_pos, p1_score, p2_pos, p2_score)
        if state in cache:
            return cache[state]

        wins = [0, 0]
        for roll, freq in {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}.items():
            new_p1_pos, new_p1_score = p1_pos, p1_score

            new_p1_pos = ((new_p1_pos + roll - 1) % 10) + 1
            new_p1_score += new_p1_pos

            new_wins = play(p2_pos, p2_score, new_p1_pos, new_p1_score)
            for i, w in enumerate(reversed(new_wins)):
                wins[i] += w * freq

        cache[state] = wins
        return wins

    positions = parse_input(input)
    return max(play(positions[0], 0, positions[1], 0))


def parse_input(input):
    return [int(line[-2:]) for line in input.splitlines()]
