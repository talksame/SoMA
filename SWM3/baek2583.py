'''
영역 탐색
1. 큐로 풀 것.
'''
from _collections import deque

w, h, case = map(int, input().split())
matrix = [[0]*h for i in range(w)]

def add(matrix, list):
    for i in range(list[1], list[3], 1):
        for s in range(list[0], list[2], 1):
            if matrix[i][s] != 1:
                matrix[i][s] = 1
    return matrix

for i in range(case):
    tmp = list(map(int, input().split()))
    matrix = add(matrix, tmp)


res = list()

def bfs(matrix, z):
    q = deque()
    q.append(z)
    sum = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    dp = []
    while q:
        x, y = q.popleft()
        if [x, y] not in dp:
            dp.append([x, y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = 1
                    q.append([nx, ny])


    return len(dp)

cnt = 0
for i in range(w):
    for s in range(h):
        if matrix[i][s] == 0:
            cnt += 1
            res.append(bfs(matrix, [i, s]))

print(cnt)
for i in sorted(res):
    print(i, end =' ')






