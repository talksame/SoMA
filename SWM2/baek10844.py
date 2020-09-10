n = int(input())

dp = [[0]*10 for i in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1



for i in range(2, n+1):
    for s in range(10):
        if s == 0:
            dp[i][s] = dp[i - 1][1]
        elif s == 9:
            dp[i][s] = dp[i-1][8]
        else:
            dp[i][s] = (dp[i-1][s-1] + dp[i-1][s+1]) % 1000000000


res = 0
for i in range(10):
    res += dp[n][i]

print(res%1000000000)
