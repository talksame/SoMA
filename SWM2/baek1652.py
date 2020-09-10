'''
백준 1652번 누울자리를 찾아라

1. 배열로 나타내서, 2칸이상 연속될 경우, cnt + 1
2. 가로나 세로일 때, 중간에 벽이 한칸 있다고 하면 다음 칸이 2칸 이상일때 +1
3. 반복문 2개로 풀 것.
'''

n = int(input())
room = list()

cnt_w = 0
cnt_h = 0

res_w = 0
res_h = 0

for i in range(n):
    room.append(input())

for i in range(n):
    for j in range(n):
        if room[i][j] == '.':
            cnt_w += 1
        else:
            if cnt_w > 1:
                res_w += 1
            cnt_w = 0
    if cnt_w > 1:
        res_w += 1
    cnt_w = 0


for i in range(n):
    for j in range(n):
        if room[j][i] == '.':
            cnt_h += 1
        else:
            if cnt_h > 1:
                res_h += 1
            cnt_h = 0
    if cnt_h > 1:
        res_h += 1
    cnt_h = 0


print(res_w , res_h)

