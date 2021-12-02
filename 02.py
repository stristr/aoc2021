# 243/732
# 2:00/4:44
from sys import stdin


def parse(line):
    dir, n = line.split(' ')
    return dir, int(n)


x, y, by, A = 0, 0, 0, 0
for dir, n in map(parse, stdin.read().strip().split('\n')):
    x += n if dir == 'forward' else 0
    y += n * (1 if dir == 'down' else -1 if dir == 'up' else 0)
    A += n * (1 if dir == 'down' else -1 if dir == 'up' else 0)
    by += A * n if dir == 'forward' else 0
print('a', x * y)
print('b', x * by)
