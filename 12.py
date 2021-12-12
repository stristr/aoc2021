# 904/379
# 15:26/18:35
from sys import stdin
from collections import defaultdict

edges = defaultdict(list)
for l, r in map(lambda line: list(line.split('-')), stdin.read().strip().split('\n')):
    edges[l] += [r]
    edges[r] += [l]

def count(current, path, max_dupes=0):
    if current.islower() and current in path:
        if path.count(current) > max_dupes or current == 'start':
            return 0
        elif path.count(current) == max_dupes:
            max_dupes = 0
    if current == 'end':
        return 1
    return sum(count(next, path + [current], max_dupes=max_dupes) for next in edges.get(current, []))

print('a', count('start', []))
print('b', count('start', [], max_dupes=1))
