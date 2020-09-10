#baek 11066 merge novel

import sys

case = int(sys.stdin.readline())
res = list()
for i in range(case):
    n = int(sys.stdin.readline())
    novel = list(map(int, sys.stdin.readline().split()))
    dp = [0 for i in range(n+1)]
    