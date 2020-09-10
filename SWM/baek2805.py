#baek2805 cutting tree

import sys


tree, need = map(int , sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))


def getTree( a ):
    sum = 0
    for i in trees:
        if i - a > 0:
            sum += (i - a)
    return sum


low = 0
max = max(trees)
ans = 0

while low <= max:
    mid = (low + max)//2
    sum = getTree(mid)

    if sum < need:
        max = mid - 1
    if sum >= need:
        ans = mid
        low = mid + 1

sys.stdout.write(str(ans))