#baekjoon11057
'''
숫자를 표로 그려보자
생각보다 규칙은 쉽게 찾을 수 있다.

'''

n = int(input())
s = [[0] * 10 for i in range(1001)]

for i in range(10):
    s[1][i] = 1


for i in range(2, n+1):
    s[i][0] = 1
    for j in range(1, 10):
        s[i][j] = s[i-1][j] + s[i][j-1]

print(sum(s[n]) % 10007)