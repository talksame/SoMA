import itertools

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result


n = int(input())
cmd = list(map(int, input().split()))
temp = list()
for i in range(1, n+1):
    temp.append(i)
res = permute(temp)
res.sort()

if cmd[0] == 1:
    print(res[cmd[1]-1])
else:
    find = cmd[1:5]
    temp = res.index(find)
    print(temp+1)