#baekjoon 2178
x, y = map(int, input().split())

matrix = [[0]*y for i in range(x)]
for i in range(x):
    temp = input()
    for j in range(y):
        matrix[i][j] = int(temp[j])

foot_print = [[0]*y for i in range(x)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


arr = []
arr.append((0,0))
foot_print[0][0] = 1

while arr:
    a, b= arr.pop(0)
    if a == x-1 and b == y-1:
        #위치가 0에서 0으로 이동할 경우, 이동거리는 1임
        print(foot_print[a][b])
        break

    for i in range(4):
        #4 방향의 각각의 값들을 구해본다.
        ax = a+dx[i]
        ay = b + dy[i]
        if ax>=0 and ax < x and ay >= 0 and ay < y:
            if foot_print[ax][ay] == 0 and matrix[ax][ay] == 1:
                foot_print[ax][ay] = foot_print[a][b] + 1
                arr.append((ax,ay))





