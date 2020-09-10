from itertools import combinations


def combination(data, k):
    num = 1
    den = 1
    k = min(data-k, k) #조합의 대칭성을 이용하여 더 적은 수의 연산을 하기 위해서입니다.
    for i in range(1, k+1):
        den *= i
        num *= data+1-i
    return int(num/den)


case = int(input())
res = list()

for i in range(case):
    left, right = map(int, input().strip().split())
    print(combination(right, left))
