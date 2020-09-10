#baek10409

case, need = map(int, input().split())

time = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(case):
    if sum + time[i] > need:
        break
    sum += time[i]
    cnt += 1

print(cnt)