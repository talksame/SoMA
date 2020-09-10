#baekjoon 6603
import sys
from itertools import combinations

input = sys.stdin.readline
flag = True


while flag:
    case = list(map(int, input().strip().split()))

    if case[0] == 0:
        flag = False
        break

    for i in combinations(case[1:] , 6):
        print(' '.join(map(str,i)))
    print()









