'''
백준 1965 점점 증가하는 수열의 최장길이 구하기

1. 증가하는 수열 구하기

'''

n = int(input())
case = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if case[i] > case[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))