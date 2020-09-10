'''
백준 1012
1. 큐로 풀어갈 것.
2. 주변의 모든 배추들이 0일때 case++
3. 배추를 한 번 탐색하면 0으로 수정해주기.
'''

from _collections import deque


move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(matrix, st):

    q = deque()
    q.append(st)

    while q:
        y, x = q.popleft()
        matrix[y][x] = 0

        for i in move:
            nx = x + i[1]
            ny = y + i[0]

            if 0 <= nx < width and 0 <= ny < height and matrix[ny][nx]:
                q.append((ny, nx))
                matrix[ny][nx] = 0
    return 1


case = int(input())
res = list()
for i in range(case):
    width, height, n = map(int, input().split())
    matrix = [[0 for _ in range(width)] for s in range(height)]

    for _ in range(n):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    count = 0

    for y in range(height):
        for x in range(width):
            if matrix[y][x] == 1:
                count += bfs(matrix, (y, x))
    res.append(count)

for i in res:
    print(i)





