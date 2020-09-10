from _collections import deque

b = [
    [(0,1), (1,0), (1,1)],
    [(0,1), (0,2), (0,3)],
    [(1,0), (2,0), (3,0)],
    [(0,1), (0,2), (1,0)],
    [(0,1), (0,2), (-1,2)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (0,2), (1,2)],
    [(1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1)],
    [(0,1), (1,0), (2,0)],
    [(1,0), (2,0), (2,-1)],
    [(1,0), (1,1), (2,1)],
    [(0,1), (1,0), (-1,1)],
    [(0,1), (1,0), (1,-1)],
    [(0,1), (1,1), (1,2)],
    [(0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,-1)],
    [(1,0), (2,0), (1,-1)],
    [(1,0), (1,1), (2,0)]
]


def bfs(x, y):
    global ans
    for i in range(19):
        temp = matrix[x][y]

        for j in range(3):
            try:
                nx = x + b[i][j][0]
                ny = y + b[i][j][1]
                temp += matrix[nx][ny]
            except IndexError:
                continue
        ans = max(ans, temp)

n, m = map(int, input().split())
matrix = list()
for i in range(n):
    matrix.append(list(map(int, input().split())))

ans = 0

for i in range(n):
    for s in range(n):
        bfs(i, s)


print(ans)

