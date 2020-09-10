#baekjoon 2293 Coin1 DP

a, b = map(int, input().split())

coin = []
for i in range(a):
    coin.append(int(input()))

dp = [0 for i in range(b+1)]
dp[0] = 1

for i in coin:
    #해당 코인부터 다음 코인을 더하기
    for j in range(1, b + 1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[b])
