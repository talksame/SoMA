'''
양방향 큐 구현

'''

from _collections import deque



n, m = map(int, input().split())
num = list(map(int, input().split()))

idx = 0

def left(a):
    global idx
    idx += 1
    temp = a.pop(0)
    a.append(temp)

def right(a):
    global idx
    idx += 1
    tmp = [a.pop(-1)]
    tmp.extend(a)
    a = tmp

    return a


n = list(range(1, n+1))

while num:
    if n[0] == num[0]:
        n.pop(0)
        num.pop(0)
    else:
        if n.index(num[0]) <= len(n)//2:
            while n[0] != num[0]:
                left(n)
        else:
            while n[0] != num[0]:
                n = right(n)

print(idx)



