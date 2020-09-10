'''
백준 뒤집힌 덧셈
1. x에 대한 역순을 받음

'''


def Rev(a):
    temp = str(a)
    temp = list(temp)
    temp.reverse()
    res = ''
    for i in range(len(temp)):
        res += temp[i]

    return int(res)


a, b = map(int, input().split())

print(Rev(Rev(a) + Rev(b)))