# 133/322
# 5:22/19:28
from sys import stdin
from collections import Counter

raw_template, rules = stdin.read().strip().split('\n\n')
f, l = raw_template[0], raw_template[-1]
template = Counter([raw_template[i:i+2] for i in range(len(raw_template) - 1)])
m = {}
for rule in rules.split('\n'):
    l, r = rule.split(' -> ')
    m[l] = [l[0] + r, r + l[1]]

def solve(template):
    s = Counter([raw_template[0], raw_template[-1]])
    for k, v in template.items():
        for c in k:
            s[c] += v
    return (max(s.values()) - min(s.values())) // 2

def tick(template):
    s = Counter()
    for k, v in template.items():
        for result in m[k]:
            s[result] += v
    return s

for _ in range(10):
    template = tick(template)
print('a', solve(template))
for _ in range(30):
    template = tick(template)
print('b', solve(template))
