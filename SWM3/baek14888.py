'''
연산자 끼워넣기
'''
from itertools import permutations

def add(a , b):
    return a + b

def sub(a,b):
    return a - b

def div(a,b):
    flag  =0
    if (a < 0 and b > 0) or (a > 0 and a < b):
        flag = 1

    a = abs(a)
    b = abs(b)
    if flag == 1:
        return -(a//b)
    else:
        return a//b

def mul(a, b):
    return a * b


case = int(input())
num = list(map(int,input().split()))
oper = list(map(int,input().split()))
command = list()
for i in range(4):
    command += [i+1]*oper[i]

command_list = list()
for i in list(permutations(command)):
    command_list.append(i)

#w중복제거하기.
command_list = list(set(command_list))

max_answer = -1000000001
min_answer = 1000000001

for i in command_list:
    answer = i[0]

    for s in range(case-1):
        if i[s] == 1:
            answer = add(answer, num[i + 1])
        elif i[s] == 2:
            answer = sub(answer, num[i + 1])
        elif i[s] == 3:
            answer = mul(answer, num[i + 1])
        else:
            answer = div(answer, num[i + 1])

        if answer < min_answer:
            min_answer = answer
        if answer > max_answer:
            max_answer = answer

print(max_answer)
print(min_answer)