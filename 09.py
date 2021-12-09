# 985/206
# 7:52/13:06
from sys import stdin
from itertools import product
from collections import deque
from math import prod

data = list(map(lambda line: list(map(int, list(line))), stdin.read().strip().split('\n')))
h, w = len(data), len(data[0])
adjacencies = lambda x, y: [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= x + dx < w and 0 <= y + dy < h]

minima, basins = [(x, y) for x, y in product(range(w), range(h))
    if all(data[y][x] < data[ay][ax] for ax, ay in adjacencies(x, y))], []

for x, y in minima:
    seen, q = set(), deque([(x, y)])
    while q:
        x, y = q.popleft()
        if data[y][x] == 9 or (x, y) in seen:
            continue
        seen.add((x, y))
        for x, y in adjacencies(x, y): 
            q.append((x, y))
    basins.append(len(seen))

print('a', sum(data[y][x] + 1 for x, y in minima))
print('b', prod(sorted(basins)[-3:]))
