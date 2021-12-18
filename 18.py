# 132/136
# 43:25/47:19
from sys import stdin
from itertools import permutations
from functools import reduce

adjacent_pairs = lambda tracker: zip(tracker, tracker[1:])
magnitude = lambda assignment: assignment if isinstance(assignment, int) else 3 * magnitude(assignment[0]) + 2 * magnitude(assignment[1])

def parse(val, addr, tracker):
    if isinstance(val, int):
        tracker.append((addr, val))
    else:
        parse(val[0], addr + [0], tracker)
        parse(val[1], addr + [1], tracker)
    return tracker

def unparse(tracker):
    result = []
    for addr, val in tracker:
        p = result
        for i in addr[:-1]:
            p += [[]] if len(p) <= i else []
            p = p[i]
        p.append(val)
    return result

homework = [parse(problem, [], []) for problem in map(eval, stdin.read().strip().split('\n'))]

def process(tracker):
    while True:
        reduced = False
        for i, ((laddr, lval), (raddr, rval)) in enumerate(adjacent_pairs(tracker)):
            if len(laddr) == len(raddr) > 4:
                if i > 0:
                    addr, val = tracker[i - 1]
                    tracker[i-1] = (addr, val + lval)
                if i < len(tracker) - 2:
                    addr, val = tracker[i + 2]
                    tracker[i+2] = (addr, val + rval)
                tracker, reduced = tracker[:i] + [(laddr[:-1], 0)] + tracker[i+2:], True
                break
        if reduced: continue
        
        for i, (addr, val) in enumerate(tracker):
            if val >= 10:
                tracker, reduced = tracker[:i] + [(addr + [0], val // 2), (addr + [1], (val + 1) // 2)] + tracker[i+1:], True
                break
        if reduced: continue

        return tracker

nest = lambda tracker, x: [([x] + addr, val) for addr, val in tracker]
add = lambda a, b: process(nest(a, 0) + nest(b, 1))

print('a', magnitude(unparse(reduce(add, homework))))
print('b', max(magnitude(unparse(add(a, b))) for a, b in permutations(homework, 2)))
