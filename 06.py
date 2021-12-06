# 491/802
# 4:41/12:24
from sys import stdin
from collections import Counter

N = Counter(map(int, stdin.read().strip().split(',')))

def cycle(N, n):
    for _ in range(n):
        M = Counter()
        for k, v in N.items():
            m = k - 1 if k > 0 else 6
            M += Counter({m: v})
            if k == 0:
                M += Counter({8: v})
        N = M
    return sum(N.values())

print('a', cycle(N, 80))
print('b', cycle(N, 256))
