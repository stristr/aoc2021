# 388/172
# 13:19/14:34
from sys import stdin
from re import findall
from itertools import product

x1, x2, y1, y2 = map(int, findall('[-\d]+', stdin.read().strip()))
M = max(abs(y1), abs(y2)) + 1
a, b = 0, 0
for x, y in product(range(1, x2 + 1), range(-M, M)):
    sx, sy, m = 0, 0, 0
    while sy >= y1 and sx <= x2:
        sx += x
        sy += y
        m = max(sy, m)
        x = max(x - 1, 0)
        y -= 1
        if x1 <= sx <= x2 and y1 <= sy <= y2:
            a = max(a, m)
            b += 1
            break
print('a', a)
print('b', b)