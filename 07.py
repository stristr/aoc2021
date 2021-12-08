# 812/1469
# 7:28/24:34
from sys import stdin
from statistics import median

nums = list(sorted(list(map(int, stdin.read().strip().split(',')))))
m = int(median(nums))
print('a', sum(abs(m - n) for n in nums))
print('b', min(sum(abs(x - n) * (abs(x - n) + 1) // 2 for n in nums) for x in range(min(nums), max(nums))))
