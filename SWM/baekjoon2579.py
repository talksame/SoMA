#2579 baek DP


n = int(input())

dp = [0 for i in range(n+1)]
score = list()

for i in range(n):
    score.append(int(input()))

dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0]+score[2] , score[1] + score[2])

for i in range(3, n):
    dp[i] = max( dp[i-2] + score[i], dp[i-3] + score[i] + score[i-1] )

print(dp[n-1])