# 147/133
# 1:07:32/1:11:14
from sys import stdin
from re import findall
from itertools import product, permutations, combinations

chunks = stdin.read().strip().split('\n\n')
data = [set(tuple(map(int, findall('[-\d]+', line))) for line in chunk.split('\n')[1:]) for chunk in chunks]

perms, signs = list(permutations((0, 1, 2))), list(product([1, -1], [1, -1], [1, -1]))
orientations = list(product(perms, signs))
transforms = lambda scanner: [[(point[i]*si, point[j]*sj, point[k]*sk) for point in scanner] for (i, j, k), (si, sj, sk) in orientations]
manhattan = lambda a, b: sum(abs(x - y) for x, y in zip(a, b))

def absorb(ref, scanner):
    for transform in transforms(scanner):
        for (ax, ay, az), (bx, by, bz) in product(ref, transform):
            dx, dy, dz  = ax - bx, ay - by, az - bz
            relative = set((x + dx, y + dy, z + dz) for x, y, z in transform)
            if len(ref & relative) >= 12:
                return ref | relative, (dx, dy, dz)
    return ref, None

ref, scanners, locations = data[0], data[1:], [(0, 0, 0)]
while scanners:
    for scanner in scanners:
        ref, location = absorb(ref, scanner)
        if location:
            locations.append(location)
            scanners.remove(scanner)

print('a', len(ref))
print('b', max(manhattan(a, b) for a, b in combinations(locations, 2)))
