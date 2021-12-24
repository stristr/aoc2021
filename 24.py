# 780/739
# 2:26:06/2:31:48

from sys import stdin

lines = stdin.read().strip().split('\n')
c, n = 18, 14
vals = [[int(op.split(' ')[-1]) for op in [lines[i+4], lines[i+5], lines[i+15]]] for i in range(0, n*c, c)]
display = lambda x: ''.join(str(x[i]) for i in range(n))

# (see 24.txt)
stack, rules, a, b = [], {}, {}, {}
for i in range(n):
    d, s, C = vals[i]
    if d == 1:
        stack.append((i, C))
    else:
        lasti, lastC = stack.pop()
        rules[i] = (lasti, lastC+s)
        rules[lasti] = (i, -lastC-s)

for i in range(n):
    a[i] = 9 + min(rules[i][1], 0)
    a[rules[i][0]] = a[i] - rules[i][1]
    b[i] = 1 + max(rules[i][1], 0)
    b[rules[i][0]] = b[i] - rules[i][1]

print ('a', display(a))
print ('b', display(b))
