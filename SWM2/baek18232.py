'''
백준 18231 파괴된 도시
'''

city, road = map(int, input().split())

matrix = [[0]*(city+1) for i in range(city+1)]


for i in range(road):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

cnt = int(input())
cand = list(map(int, input().split()))

res = list()

for i in range(1, city+1):
    if i not in cand:
        res.append(i)

for i in range(city+1):
    for s in range(city+1):
        if matrix[i][s] == 1 and i in res:
            res.append(s)

for i in res:
    if i in cand:
        cand.remove(i)

if len(cand) == 0:
    print(-1)
else:
    print(len(cand))
    for i in cand:
        print(i, end=' ')
