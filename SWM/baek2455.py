#baekjoon 2455 지능형 기차


tmp1, tmp2= map(int, input().split())
max = tmp2
now = tmp2
for i in range(3):
    peopleIn, peopleOut = map(int, input().split())
    now = now - peopleIn + peopleOut
    if now > max:
        max = now

print(max)
