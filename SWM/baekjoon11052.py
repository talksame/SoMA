#baekjoon 11052 DP
'''
카드의 index를 맞춰줘서 풀기 쉽게 할 것.
인덱스를 기준으로 앞에 있는 값중에서 가장 큰 값 + 현재의 카드의 값을
더해서 풀어주는 것이 중요함.

'''

n = int(input())

res = [0] + [0 for i in range(n+1)]
price = [0] + list(map(int, input().split()))

res[1] = price[1]

for i in range(2, n + 1):
    for j in range(1, i+1):
        if res[i] < res[i-j]+price[j]:
            res[i] = res[i-j]+price[j]

print(res[n])