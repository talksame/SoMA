'''
백준 18228 팽귄

'''


case = int(input())
ice = list(map(int, input().split()))
p = ice.index(-1)
left = min(ice[0:p])
right = min(ice[p+1:])
print(left + right)