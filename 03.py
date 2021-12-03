# 1976/894
# 8:12/19:51
from sys import stdin
from copy import copy


data = list(stdin.read().strip().split('\n'))
n = len(data[0])
gamma, epsilon = '', ''
for i in range(n):
    ones, zeros = sum(seq[i] == '1' for seq in data), sum(seq[i] == '0' for seq in data)
    gamma += '1' if ones > zeros else '0'
    epsilon += '0' if ones > zeros else '1'

o, co2 = copy(data), copy(data)
for i in range(n):
    ones, zeros = sum(seq[i] == '1' for seq in o), sum(seq[i] == '0' for seq in o)
    o = [seq for seq in o if seq[i] == ('1' if zeros <= ones else '0')]
    if len(o) == 1:
        break
for i in range(n):
    ones, zeros = sum(seq[i] == '1' for seq in co2), sum(seq[i] == '0' for seq in co2)
    co2 = [seq for seq in co2 if seq[i] == ('0' if zeros <= ones else '1')]
    if len(co2) == 1:
        break

print('a', int(epsilon, 2) * int(gamma, 2))
print('b', int(o[0], 2) * int(co2[0], 2))
