# 1605/440
# 1:46:19/1:47:58
from sys import stdin
from collections import deque
from math import inf
from re import findall

lines = stdin.read().strip().split('\n')
data = [findall('[ABCD]', line) for line in lines[2:-1]]
depth, depths = len(data), list(reversed(range(len(data))))
hall = [0, 1, 3, 5, 7, 9, 10]
state = [None if i in hall else [data[j][i // 2 - 1] for j in range(len(data))] for i in range(11)]
scores = {c: 10 ** (ord(c) - ord('A')) for c in 'ABCD'}
target_index = {c: (ord(c) - ord('A') + 1) * 2 for c in 'ABCD'}
target_char = {v: k for k, v in target_index.items()}
has_path = lambda a, b: all(state[i] is None for i in range(a, b) if i in hall)
hash = lambda l: tuple(tuple(v) if isinstance(v, list) else v for v in l)

q, M, seen = deque([[state, 0]]), inf, {}

while q:
    state, score = q.popleft()
    h = hash(state)
    if score >= M or seen.get(hash(state), inf) <= score:
        continue
    seen[h] = score
    if all(all(c == k for c in state[v]) for k, v in target_index.items()):
        M = min(M, score)
        continue
    for n in range(11):
        if n in hall and state[n] is not None:
            c = state[n]
            dest = target_index[c]
            if has_path(min(dest, n) + 1, max(dest, n)):
                for d in depths:
                    if state[dest][d] is None:
                        next_state = state.copy()
                        next_state[dest] = state[dest][:d] + [c] + state[dest][d+1:]
                        next_state[n] = None
                        q.append((next_state, score + (abs(dest - n) + depth - d) * scores[c]))
                        break
                    elif state[dest][d] != c:
                        break
        elif n not in hall and any(state[n][d] != target_char[n] and state[n][d] is not None for d in depths):
            d = next(d for d, v in enumerate(state[n]) if v is not None)
            for k in hall:
                if state[k] is not None:
                    continue
                if has_path(min(k, n), max(k, n)):
                    c = state[n][d]
                    next_state = state.copy()
                    next_state[n] = state[n][:d] + [None] + state[n][d+1:]
                    next_state[k] = c
                    q.append((next_state, score + (abs(k - n) + depth - d) * scores[c]))

print(M)
