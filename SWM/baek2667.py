#baek2667

b = int(input())


def dfs(matrix, cnt, x, y):
    matrix[x][y] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        temp1 = x + dx[i]
        temp2 = y + dy[i]

        if temp1 >= 0 and temp1 < b and temp2 >= 0 and temp2 < b:
            if matrix[temp1][temp2] == 1:
                cnt = dfs(matrix, cnt+1, temp1, temp2)

    return cnt

matrix = [[0]*b for i in range(b)]

for i in range(b):
    temp = input()
    for s in range(len(temp)):
        matrix[i][s] = int(temp[s])

res = list()

for i in range(b):
    for j in range(b):
        if matrix[i][j] == 1:
            res.append(dfs(matrix, 1, i ,j))

print(len(res))
for i in sorted(res):
    print(i)

