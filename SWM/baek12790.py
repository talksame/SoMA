#baekjoon 12790 Super Fantasy war

import sys

def power (hp , mp, attack, amor):
    return (hp*1)+ (5*mp) + (2 * attack) + (2 * amor)

def getHP( a ):
    if a[0] + a[4] <= 1:
        return 1
    else:
        return a[0] + a[4]

def getMP( a ):
    if a[1] + a[5] <= 1:
        return 1
    else:
        return a[1] + a[5]

def getAt( a ):
    if a[2] + a[6] <= 0:
        return 0
    else:
        return a[2] + a[6]

def getAM(a):
    return a[3] + a[7]

n = int(sys.stdin.readline())
res = list()
for i in range(n):
    human = list(map(int, sys.stdin.readline().split()))
    res.append(power(getHP(human), getMP(human), getAt(human), getAM(human)))

for i in range(n):
    print(res[i])