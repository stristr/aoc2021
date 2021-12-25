# 279/241
# 12:37/12:43
from sys import stdin
from itertools import product

lines = stdin.read().strip().split('\n')
h, w = len(lines), len(lines[0])
m = {(x, y): lines[y][x] for x, y in product(range(w), range(h))}
a = 0
east = lambda x, y: ((x + 1) % w, y)
south = lambda x, y: (x, (y + 1) % h)

while True:
    moved, a = False, a + 1
    M = m.copy()
    for x, y in product(range(w), range(h)):
        if m[x, y] == '>' and m[east(x, y)] == '.':
            M[x, y] = '.'
            M[east(x, y)] = '>'
            moved = True
    N = M.copy()
    for x, y in product(range(w), range(h)):
        if M[x, y] == 'v' and M[south(x, y)] == '.':
            N[x, y] = '.'
            N[south(x, y)] = 'v'
            moved = True
    if not moved:
        break
    m = N
print('a', a)
