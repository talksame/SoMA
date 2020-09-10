import sys
input = sys.stdin.readline
from collections import deque
import copy
import itertools


a, b = map(int, input().split())
arr = [i for i in range(a)]


check = list(itertools.combinations(arr, b))

cnt = 0
for i in check:
    tmp = sum(i)
    if tmp%a == 0:
        cnt += 1

print(cnt)