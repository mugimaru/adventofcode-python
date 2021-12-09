# [Advent Of Code](https://adventofcode.com) solutions in Python

## Setup

```
pip install poetry
python -m poetry install
python -m poetry shell
```

## Usage

with my inputs

```
python aoc/cli.py --year 2021 5
```

with inputs from stdin

```
cat input.txt | python aoc/cli.py --year 2021 5
```

with custom input path

```
python aoc/cli.py --year 2021 --input-path /path/to/file.txt 5
```
