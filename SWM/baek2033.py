#baekjoon 2033 round

n = int(input())
case = input()
cnt = 1
i = 0
while True:
    if i > n-1:
        break
    if case[i] == 'S':
        i += 1
        cnt += 1
    elif case[i] == 'L':
        i += 2
        cnt += 1
print(cnt)
