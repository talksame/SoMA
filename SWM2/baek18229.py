'''
baekjoon 18229
내가 살께
'''

a, b, find = map(int, input().split())

people = list()
for i in range(a):
    people.append(list(map(int, input().split())))

res = [ 0 for i in range(a+1)]
cnt = 0
idx = 0
for i in range(0, b):
    for s in range(0, a):
        res[s] += people[s][i]
        if res[s] >= find:
            cnt = i
            idx = s
            break
    if res[idx] >= find:
        break


print(idx + 1, cnt + 1)