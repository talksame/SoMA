'''
#백준 9251

LCS 알고리즘의 시작은
2차원 배열을 통해서 작은 값들을 찾아가는 것.


'''



a = input()
b = input()

dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]


for i in range(1, len(a) + 1):
    for s in range(1, len(b) + 1):
        if a[i-1] == b[s-1]:
            dp[i][s] = dp[i-1][s-1] + 1
        else:
            dp[i][s] = max(dp[i-1][s], dp[i][s-1])

print(dp[-1][-1])
