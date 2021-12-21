# 1000/119
# 12:11/21:45
from sys import stdin
from itertools import product
from collections import Counter
from functools import cache

input = list(map(lambda line: int(line[-1]), stdin.read().strip().split('\n')))
normalize = lambda x, n: (x - 1) % n + 1
positions, scores, roll, turn = input.copy(), [0, 0], 0, 0

while max(scores) < 1000:
    p, s = turn % 2, sum(normalize(roll + i, 100) for i in range(1, 4))
    positions[p] = normalize(positions[p] + s, 10)
    scores[p] += positions[p]
    roll += 3
    turn += 1
print('a', min(scores) * roll)

quants = list(Counter(map(sum, product(*([[1, 2, 3]] * 3)))).items())

@cache
def quantize(positions, scores):
    win, lose = 0, 0
    for k, v in quants:
        p = normalize(positions[0] + k, 10)
        s = scores[0] + p
        if s >= 21:
            win += v
        else:
            qlose, qwin = quantize((positions[1], p), (scores[1], s))
            win += qwin * v
            lose += qlose * v
    return win, lose

print('b', max(quantize(tuple(input), (0, 0))))
