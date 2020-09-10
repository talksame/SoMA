#baekjoon 1713 candidate

n = int(input())
case = int(input())

cand = [0 for i in range(10)]
res = list()
add = list(map(int, input().split()))

for i in add:
    if i not in res and len(res) == 3:
        cand[res[0]] = 0
        del res[0]
        res.append(i)
        cand[i] += 1
    elif i not in res and len(res) < 3:
        res.append(i)
        cand[i] += 1
    elif i in res:
        cand[i] += 1

res.sort()
for i in range(n):
    find = cand.index(max(cand))
    print(cand[find])
    cand[find] = 0


