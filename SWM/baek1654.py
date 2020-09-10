#baekjoon 1645 Cutting Lan

import sys

n, m = map(int, sys.stdin.readline().split())
res = []

for s in range(n):
    res.append(int(sys.stdin.readline()))

low = 1
max = max(res)

result = 0

while low <= max:
    # 임시로 정한 랜선의 길이
    mid = (low + max) // 2

    sum = 0
    for i in res:
        sum += (i // mid)

    # 갯수가 찾고자 하는 갯수보다 클 경우에는 작은 값을 변경
    # 갯수가 찾고자 하는 갯수보다 작을 경우애는 큰 값을 변경해준다..
    if sum >= m:
        result = mid
        low = mid + 1
    elif sum < m:
        max = mid - 1

print(result)