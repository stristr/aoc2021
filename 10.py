# 3066/1076
# 14:40/16:07
from sys import stdin

lines = stdin.read().strip().split('\n')
a = {')': 3, ']': 57, '}': 1197, '>': 25137}
b = {')': '1', ']': '2', '}': '3', '>': '4'}
opps = {')': '(', ']': '[', '}': '{', '>': '<', '(': ')', '[': ']', '{': '}', '<': '>'}

def classify(line):
    s = []
    for c in line:
        if c in '{([<':
            s.append(c)
        elif s[-1] != opps[c]:
            return c, None
        else:
            s.pop()
    return None, int(''.join(b[opps[c]] for c in reversed(s)), 5)

m = [classify(line) for line in lines]
points = sorted(p for _, p in m if p is not None)

print('a', sum(a[c] for c, _ in m if c is not None))
print('b', points[len(points) // 2])
