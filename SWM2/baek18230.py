'''
baekjoon 18230
타일링하기
'''

find, a, b = map(int, input().split())

size = 2 * find

one = list(map(int, input().split()))
two = list(map(int, input().split()))
one.sort(reverse= True)
two.sort(reverse= True)

res = 0
sum = 0

while True:
    if res == size:
        break
    elif res == size-2:
        sum += one[0]
        break

    tmp = one[0] + one[1]

    if tmp > two[0]:
        res += 4
        sum += tmp
        del one[0]
        del one[0]
    else:
        res += 4
        sum += two[0]
        del two[0]

print(sum)