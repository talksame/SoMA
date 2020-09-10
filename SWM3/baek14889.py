'''
순열로 풀 것.
'''

from itertools import permutations

n = int(input())
matrix = list()
for i in range(n):
    matrix.append(list(map(int, input().split())))



people = [i for i in range(1, n+1)]
case = list(permutations(people))

min = 100001
teamsize = n/2



print(min)
