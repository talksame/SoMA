import sys
input = sys.stdin.readline


n = int(input())
num = [0]*10
tmp = list(map(int, input().split()))

for i in tmp:
    num[i-1] += 1

cnt = 0
for i in range(10):
    if num[i] != 0:
        cnt += 1

if cnt >= 3:
    print("YES")
else:
    print("NO")
