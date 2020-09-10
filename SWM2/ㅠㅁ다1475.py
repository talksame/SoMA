'''
백준 1475
'''

import math
n = input()
ans = list(n)
res = [0 for i in range(10)]

for i in ans:
    temp = int(i)
    res[temp]  += 1
    res[6] += res[9]
    res[9] = 0

if res[6] != 0:
    res[6] /= 2

print(math.ceil(max(res)))

