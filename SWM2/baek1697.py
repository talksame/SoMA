'''
숨바꼭질
1. 이제는 bfs는 큐로 푼다.
2. popleft()
넣고 검색하고,dp에 추가한다.
검색은 문제에서 요구하는대로 검색하자.
'''
from _collections import deque

def bfs(dp, n, m):
    q = deque()
    q.append(n)

    while q:
        i = q.popleft()
        if i == m:
            return dp[i]
        for j in (i + 1, i-1, i*2):
            if ( 0 <= j < 100001) and dp[j] == 0:
                dp[j] = dp[i] + 1
                q.append(j)

n, m = map(int, input().split())
dp = [0] * 100001
res = bfs(dp, n, m)
print(res)
