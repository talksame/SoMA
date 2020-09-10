'''
백준 3190
뱀 구하기
'''

from _collections import deque
n = int(input())
matrix = [[0]*n for i in range(n)]
apple = int(input())
for i in range(apple):
    a, b = map(int, input().split())
    matrix[a][b] = 1

for i in range(n):
    print(matrix[i])

case = int(input())
dp = []
snake = [0,0]
for i in range(case):
    command = list(map(input().split()))

    q = deque()
    








