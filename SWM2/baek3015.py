'''
baekjoon3015
1. 반복문 1개와 while 한개로 만들어 나갈것.
2. 스택을 유지할 것.

n = int(input())

people = list()

for i in range(n):
    people.append(int(input()))

dp = []
res = 0
for i in range(n):
    temp = people[i]
    j = i + 1
    #print(people[i])
    while j < n:
        #print(people[j])
        if people[j] > temp:
            res += 1
            break
        else:
            res+=1
            j += 1

print(res)

'''

n = int(input())
dp = []
res = 0

for i in range(n):
    x = int(input())
    while dp and dp[-1][0] < x:
        res += dp.pop()[1]

    if dp and dp[-1][0] == x:
        cnt = dp.pop()[1]
        res += cnt


        if len(dp) != 0:
            res += 1


        dp.append([x, cnt+1])
    else:
        if len(dp) != 0:
            res += 1
        dp.append([x, 1])

print(res)




