'''
백준 2468 안전영역
'''
from _collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(r, h):
    q = deque()
    q.append(r)
    while q:
        x, y = q.popleft()
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and not visit[nx][ny] and matrix[nx][ny] > h:
                visit[nx][ny] = 1
                q.append([nx, ny])


n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

cnt = 1

for k in range((max(map(max, matrix)))):
    visit = [[0]*n for i in range(n)]
    safe = 0
    for i in range(n):
        for s in range(n):
            if matrix[i][s] > k and not visit[i][s]:
                safe += 1
                visit[i][s] = 1
                bfs([i, s], k)
    cnt = max(cnt, safe)

print(cnt)


