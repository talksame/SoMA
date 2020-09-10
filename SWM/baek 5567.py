#baek 5032 탄산음료

import sys

a, b, c = map(int, sys.stdin.readline().split())
total = a+b
rest = 0
cnt = 0

while total >= c:
    cnt += total//c
    total = total//c + total%c

sys.stdout.write(str(cnt))


