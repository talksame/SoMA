'''

백준 2493

'''


case = int(input())
t = list(map(int, input().split()))

#계산용 DP & 결과용 DP
dp = []
res = []

for i in range(case):
    while dp:
        if dp[-1][1] > t[i]:
            res.append(dp[-1][0] + 1)
            break
        dp.pop()

    if not dp:
        res.append(0)

    dp.append([i, t[i]])

for i in range(case):
    print(res[i], end=' ')
