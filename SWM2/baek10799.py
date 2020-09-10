'''
백준 10799 쇠막대기

1. 스택으로 풀 것.
2. 현재의 괄호와 다음 괄호를 비교하고,
counting을 해줄 것.
3. index가 0일경우 맨 마지막일 경우를 고려해줄것.
'''


string = input()

dp = []
res = 0

for i in range(len(string)):
    before_str = None
    if 0 < i:
        before_str = string[i-1]
    next_str = None
    if i < len(string)-1:
        next_str = string[i+1]
    cur_str = string[i]
    if cur_str == '(':
        if next_str == ')':
            if dp:
                dp[-1] += 1
        elif next_str == '(':
            dp.append(0)

    elif cur_str == ')':
        if before_str == ')':
            temp = dp.pop()
            res += (temp + 1)
            if dp:
                dp[-1] += temp


print(res)
