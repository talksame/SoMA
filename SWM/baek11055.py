'''
백준 11055 가장 큰 증가 부분 수열

1. sum 값을 구해서 max만 남기고
2. 그 max ans 에 추가하고
3. ans에서 max 값 뽑아내기
4. 이 알고리즘은 그리디에서 생각함.

'''

n = int(input())
num_list = list(map(int, input().split()))
dp =[0 for i in range(n)]

dp[0] = num_list[0]

for i in range(1, n):
    sum = []

    for j in range(i-1, -1, -1):
        if num_list[i] > num_list[j]:
            sum.append(dp[j])
    if not sum:
        dp[i] = num_list[i]
    else:
        dp[i] = num_list[i] + max(sum)

print(max(dp))