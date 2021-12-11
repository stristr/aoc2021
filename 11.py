# 829/577
# 16:22/16:40
from sys import stdin
from itertools import product

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
m = {(x, y): int(lines[y][x]) for x, y in product(range(w), range(h))}

get_flashable = lambda: [(x, y) for (x, y), v in m.items() if v > 9]

a, t = 0, 0
while True:
    flashed = set()
    for x, y in product(range(w), range(h)):
        m[x, y] += 1
    flashable = get_flashable()
    while flashable:
        for x, y in flashable:
            m[x, y] = 0
            flashed.add((x, y))
            for ax, ay in [(x + dx, y + dy) for dx, dy in product([0, 1, -1], [0, 1, -1])]:
                if (ax, ay) != (x, y) and (ax, ay) in m and (ax, ay) not in flashed:
                    m[ax, ay] += 1
        flashable = get_flashable()
    t += 1
    a += len(flashed)
    if t == 100:
        print('a', a)
    if len(flashed) == len(m):
        print('b', t)
        break
