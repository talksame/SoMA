n = int(input())

num = list(map(int, input().split()))
dp = [0 for i in range(n)]
res = -1001
for i in range(n):
    dp[i] = max( dp[i-1] + num[i], num[i])
    res = max(res, dp[i])

print(res)

