# 299/458
# 8:31/27:01
from math import inf
from sys import stdin
from itertools import product
from collections import deque

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
wrap = lambda x, i: str(x + i if x + i < 10 else x + i - 9)

lines = [''.join(''.join(wrap(int(c), x) for c in line) for x in range(5)) for line in lines]
for y in range(1, 5):
    for line in lines[:h]:
        lines.append(''.join(wrap(int(c), y) for c in line))

m = {(x, y): int(lines[y][x]) for x, y in product(range(5*w), range(5*h))}
q = deque([(0, 0)])
visited = {(0, 0): 0}
while q:
    x, y = q.popleft()
    for xx, yy in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
        if 0 <= xx < 5 * w and 0 <= yy < 5 * h and visited.get((xx, yy), inf) > visited[x, y] + m[xx, yy]:
            q.append((xx, yy))
            visited[xx, yy] = visited[x, y] + m[xx, yy]

print('a', visited[w - 1, h - 1])
print('b', visited[5 * w - 1, 5 * h - 1])
