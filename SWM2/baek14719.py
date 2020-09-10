'''
baekjoon 14719

'''


h, w = map(int, input().split())
block = list(map(int, input().split()))

ans = 0

for i in range(len(block)):
    #왼/오른쪽으로 가장 높은 건물
    left = max(block[:i+1])
    right = max(block[i:])

    #최소값
    min_height = min(left, right)
    ans = ans + abs(block[i] - min_height)

print(ans)

