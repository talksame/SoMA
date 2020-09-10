'''
백준 1964
오각형의 점의 갯수 구하기
'''

n = int(input())

start = 0

for i in range(n+1):
    start += (i * 3) + 1

print(start%45678)