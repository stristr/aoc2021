# 752/570
# 31:52/32:13
from sys import stdin
from itertools import product

algo, rest = stdin.read().strip().split('\n\n')
lines = rest.split('\n')
h, w = len(lines), len(lines[0])
m = set((x, y) for x, y in product(range(w), range(h)) if lines[y][x] == '#')

def enhance(x, y, m, i):
    points = [(x + dx, y + dy) for dy, dx in product([-1, 0, 1], [-1, 0, 1])]
    if i % 2 == 1:
        code = int(''.join('1' if p in m else '0' for p in points), 2)
    else:
        code = int(''.join('1' if p not in m else '0' for p in points), 2)
    return algo[code] == ('.' if i % 2 == 1 else '#')

for i in range(1, 51):
    m = set((x, y) for x, y in product(range(-i, w + i + 1), range(-i, h + i + 1)) if enhance(x, y, m, i))
    if i == 2:
        print('a', len(m))
print('b', len(m))
