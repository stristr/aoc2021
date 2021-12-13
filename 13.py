# 694/272
# 12:44/13:30
from sys import stdin

xy, folds = map(lambda lines: lines.split('\n'), stdin.read().strip().split('\n\n'))
dots = set(tuple(map(int, line.split(','))) for line in xy)
folds = [(line[11], int(line[13:])) for line in folds]

for i, (axis, n) in enumerate(folds):
    if axis == 'y':
        dots = set((x, y) if y < n else (x, 2*n-y) for x, y in dots)
    else:
        dots = set((x, y) if x < n else (2*n-x, y) for x, y in dots)
    if i == 0:
        print('a', len(dots))

h, w = max(y for _, y in dots) + 1, max(x for x, _ in dots) + 1

for y in range(h):
    print(''.join('•' if (x, y) in dots else ' ' for x in range(w)))
