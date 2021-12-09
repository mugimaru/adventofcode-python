import os
import sys
import importlib
import timeit
import click

def solve(year: int, day: int, input: str):
  solution = importlib.import_module(f'aoc{year}.day{day:02d}.solution')
  return solution.part1(input), solution.part2(input)

def solve_and_report(year: int, day: int, input: str) -> None:
    started_at = timeit.default_timer()
    p1, p2 = solve(year, day, input)
    print(f'{year}/{day:02d} solved in {timeit.default_timer() - started_at}sec\n  part1 -> {p1}\n  part2 -> {p2}')

def default_input_path(year: int, day: int):
  return os.path.join(os.getcwd(), 'aoc', f'aoc{year}', f'day{day:02d}', 'input.txt')

def read_input(path) -> str:
    with open(path, 'r') as input_file:
      input = input_file.read().rstrip()
    return input

def solve_and_report_by_file_path(path):
  print(path)

@click.command()
@click.option('-y', '--year', type=int)
@click.argument('day', type=int)
@click.option('--stdin', default=False, help='Read puzzle input from stdin.')
@click.option('-p', '--input-path', default=None, help='Read puzzle input from given path.', type=click.Path(exists=True))
def main(year, day, stdin, input_path):
    year = int(year) if year else 2021
    day = int(day)

    input = sys.stdin.read().rstrip() if stdin else read_input(input_path or default_input_path(year, day))
    solve_and_report(year, day, input)

if __name__ == "__main__":
    main()