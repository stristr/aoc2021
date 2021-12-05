# 479/375
# 8:46/13:49
from sys import stdin
from re import findall
from collections import defaultdict

a, b = defaultdict(int), defaultdict(int)
sign = lambda x : 0 if x == 0 else x // abs(x)
for x1, y1, x2, y2 in map(lambda line: map(int, findall('\d+', line)), stdin.read().strip().split('\n')):
    if x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2):
        continue
    dx, dy, n = sign(x2 - x1), sign(y2 - y1), max(abs(x1 - x2), abs(y1 - y2))
    for _ in range(n+1):
        a[x1, y1] += 1 if dx == 0 or dy == 0 else 0
        b[x1, y1] += 1
        x1 += dx; y1 += dy
print('a', sum(value > 1 for value in a.values()))
print('b', sum(value > 1 for value in b.values()))
