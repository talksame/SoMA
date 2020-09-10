#baekjoon 14051 상담 잡아주기

case = int(input())

time = [0 for i in range(case)]
price = [0 for i in range(case)]
dp = [0 for i in range(case+1)]
for i in range(case):
    time[i], price[i] = map(int, input().split())


for i in range(case):
    dp[i+1] = max(dp[i] , dp[i+1])

    if i + time[i] <= case:
        dp[i+ time[i]] = max(dp[i+ time[i]], dp[i]+price[i])

print(dp[case])


