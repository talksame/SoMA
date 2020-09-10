'''
근묵자흑
'''

a, b = map(int, input().split())
num = list(map(int, input().split()))

idx = num.index(min(num))

if idx < a//2:
    left = len(num[:idx + 1])
    print(left)
    next_idx = left%(b-1) + idx
    right = len(num[next_idx:]) -1
    print(right)
else:
    right = len(num[idx:])
    print(right)
    next_idx = right%(b-1) + idx
    left = len(num[:idx-1]) -1
    print(left)

res = (left//(b-1)) + (right//(b-1)) + 1
print(res)