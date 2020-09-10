import sys

res = list()
n = int(sys.stdin.readline())

for i in range(n):
    case = int(sys.stdin.readline())
    score = list()
    for i in range(case):
        temp = list(map(float, sys.stdin.readline().split()))
        score.append(temp)
    gp = 0
    temp2 = 0
    for i in range(case):
        gp += score[i][0]
        temp2 += score[i][1]*score[i][0]

    res.append([gp, round(temp2/gp, 1)])

for i in range(n):
    print(int(res[i][0]), end=' ')
    print(res[i][1])