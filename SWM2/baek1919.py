'''
백준 1919
'''

a = input()
b = input()

if len(a) > len(b):
    temp = a
    a = b
    b = temp


def union(a, b):
    res = list()
    for i in a:
        for s in b:
            if i == s:
                res.append(i)
                break

    return res

res = union(list(a), list(b))
c = len(a) - len(res)
d = len(b) - len(res)

print(c+d)