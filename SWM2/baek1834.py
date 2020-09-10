'''
백준 1834
1. 나머지와 몫이 같은 수

'''

def find(a):
    temp = a*a
    res = list()

    for i in range(a+1, temp, a+1):
        res.append(i)
    return res



a = int(input())
res = find(a)
print(sum(res))