'''
촌수계산
'''
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    visited = [0] * (n+1)
    visited[a] = 1
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            if v == ed:
                return cnt - 1

            for i in matrix[v]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
    return -1

n = int(input())
st, ed = map(int, input().split())
case = int(input())

matrix = [[] for _ in range(n+1)]

for i in range(case):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)


print(bfs(st))
