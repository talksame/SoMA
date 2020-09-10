'''
역시 bfs 큐로 구해보자

'''
from _collections import deque


def bfs(matrix, n, i):
    visited = [0] * n
    q = deque()
    q.append(i)
    while q:
        idx = q.popleft()
        for i, v in enumerate(matrix[idx]):
            if visited[i] == 0 and v == 1:
                visited[i] = 1
                q.append(i)


    return visited



n = int(input())
matrix = list()
for i in range(n):
    a = list(map(int, input().split()))
    matrix.append(a)


for i in range(n):
    res = bfs(matrix, n, i)
    for s in range(n):
        print(res[s], end =' ')
    print()