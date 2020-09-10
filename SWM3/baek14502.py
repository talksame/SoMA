'''
백준 14502 연구소.
1. 큐로 못품.
'''

from _collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a):
    q = deque()
    q.append(a)
    x, y = a[0], a[1]
    visit[x][y] = 1
    color =  matrix[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <n) and (0 <= ny <n):
                if color == matrix[nx][ny] and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx, ny])


def bfs2(a):
    q = deque()
    q.append(a)
    x, y = a[0], a[1]
    visit[x][y] = 1
    filter = {
        'R' : 'R',
        'G' : 'R',
        'B' : 'B'
    }

    color = filter[matrix[x][y]]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx <n) and (0 <= ny <n):
                if color == filter[matrix[nx][ny]] and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append([nx, ny])



n = int(input())
matrix = list()

for i in range(n):
    matrix.append(list(input()))

visit = [[0]*(n) for i in range(n)]
colors = 0
i = 0
while i < n:
    j = 0
    while j < n:
        if visit[i][j] == 0:
            colors += 1
            bfs([i,j])
        j +=1
    i +=1



visit = [[0]*n for i in range(n)]
no_colors = 0
i = 0
while i < n:
    j = 0
    while j < n:

        if visit[i][j] == 0:
            no_colors += 1
            bfs2([i,j])
        j +=1
    i +=1

print(colors, no_colors)