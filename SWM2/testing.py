import sys
from collections import deque
'''
파이썬에서 큐를 선언하기 위해서는,
for collections import deque
q = deque

q.append()
q.pop() / 뒤에서 빼오기
q.popleft() 앞에서 빼오기

늘 조건만 조금 생각하면 풀 수 있는데
자꾸 못 푸니 좀더 꼼꼼히 생각해보는 버릇 만들기.

'''

input = sys.stdin.readline


def bfs(m, n , box):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    days = -1

    while ripe:
        days += 1

        for i in range(len(ripe)):
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if ( 0 <= nx < n) and ( 0 <= ny < m) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx, ny])
    for b in box:
        if 0 in b:
            return -1
    return days




m, n = map(int, input().split())
box, ripe = [], deque()

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            ripe.append([i,j])
    box.append(row)


print(bfs(m, n, box))