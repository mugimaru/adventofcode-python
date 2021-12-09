def part1(input):
  cols = list(map(list, zip(*input.splitlines())))
  gamma = ("".join(max(k, key = k.count) for k in cols))
  epsilon = ("".join(min(k, key = k.count) for k in cols))

  return int(gamma, 2) * int(epsilon, 2)

def part2(input):
  input = input.splitlines()
  ogr = int("".join(_calculate_rating(input, max, 0)), 2)
  co2sr = int("".join(_calculate_rating(input, min, 0)), 2)

  return ogr * co2sr

def _calculate_rating(items, fun, index):
    v = [item[index] for item in items]
    q = fun(v, key = lambda x: (v.count(x), x))
    items = [item for item in items if item[index] == q]
    if len(items) == 1:
        return items[0]
    else:
        return _calculate_rating(items, fun, index + 1)