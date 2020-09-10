'''
    백준 2225 합분해

    1.  반복문 3개로 풀기
    2.
'''

a, b = map(int, input().split())

num = [i for i in range(a)]
dp = [[0]*(a+1) for i in range(b + 1)]

for i in range(a+1):
    dp[0][i] = 1

for i in range(b + 1):
    dp[i][0] = 1

for i in range(1, b+1):
    for j in range(1, a+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


print((dp[b-1][a])%1000000000)



