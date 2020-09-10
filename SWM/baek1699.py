'''
백준 1699 제곱수의 합

1. 제곱값들을 가지고 있는 리스트를 만들 것.
2. 규칙 - 해당 인덱스 제곱값만큼 빼고 + 1
3. 만약에 인덱스 부족하면 반복문 종료 후
추가된 리스트에서 최대값을 결과값에 저장.


'''

n = int(input())
dp = [ 0 for i in range(n+1)]
save = [i * i for i in range(1, n+1)]

for s in range(1, n+1):
    ans = list()
    for j in save:
        if s < j:
            break
        ans.append(dp[s - j])
    dp[s] = min(ans) + 1

print(dp[n])

