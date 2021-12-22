# 139/1132
# 6:21/1:58:38
from sys import stdin
from re import findall
from math import prod

class Prism:
    bounds = None

    def __init__(self, bounds=None):
        self.bounds = bounds

    def volume(self):
        if self.bounds is None:
            return 0
        return prod(m2 - m1 + 1 for m1, m2 in self.bounds)

    def __and__(self, prism):
        if any(t2 < m1 or m2 < t1 for (m1, m2), (t1, t2) in zip(self.bounds, prism.bounds)):
            return Prism()
        return Prism(bounds=tuple((max(m1, t1), min(m2, t2)) for ((m1, m2), (t1, t2)) in zip(self.bounds, prism.bounds)))

    def __sub__(self, prism):
        overlap = self & prism
        if overlap.bounds is None:
            return [self]
        remainders = [
            ((self.bounds[0][0], overlap.bounds[0][0] - 1), self.bounds[1], self.bounds[2]),       # L
            ((overlap.bounds[0][1] + 1, self.bounds[0][1]), self.bounds[1], self.bounds[2]),       # R
            (overlap.bounds[0], self.bounds[1], (self.bounds[2][0], overlap.bounds[2][0] - 1)),    # D
            (overlap.bounds[0], self.bounds[1], (overlap.bounds[2][1] + 1, self.bounds[2][1])),    # U
            (overlap.bounds[0], (self.bounds[1][0], overlap.bounds[1][0] - 1), overlap.bounds[2]), # B
            (overlap.bounds[0], (overlap.bounds[1][1] + 1, self.bounds[1][1]), overlap.bounds[2]), # F
        ]
        return [Prism(bounds=bounds) for bounds in remainders if all(m1 <= m2 for m1, m2 in bounds)]

lines = stdin.read().strip().split('\n')
prisms = []
for line in lines:
    on, (x1, x2, y1, y2, z1, z2) = line[:2] == 'on', map(int, findall('[-\d]+', line))
    next = Prism(bounds=((x1, x2), (y1, y2), (z1, z2)))
    prisms = [remainder for prism in prisms for remainder in prism - next if remainder.volume() > 0] + ([next] if on else [])

initializer = Prism(bounds=[[-50, 50]] * 3)
print('a', sum((prism & initializer).volume() for prism in prisms))
print('b', sum(prism.volume() for prism in prisms))
