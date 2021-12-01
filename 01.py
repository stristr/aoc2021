# 355/168
# 1:35/3:08
from sys import stdin

data = list(map(int, stdin.read().strip().split('\n')))
print('a', sum(data[i] < data[i+1] for i in range(len(data) - 1)))
print('b', sum(data[i] < data[i+3] for i in range(len(data) - 3)))
