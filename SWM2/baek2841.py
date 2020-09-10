'''
baekjoon 2841 외계인의 기타연구

1. line이 같은 경우에는 pret을 검색
- pret이 크다면 append
- pret이 작다면 pop
2. line이 다른 경우에는 스택을 초기화 &

'''


case, pret = map(int, input().split())


dp = [[0] for i in range(6)]

res = 0

for i in range(case):
    x, y = map(int, input().split())
    x -= 1
    while dp and dp[x][-1] > y:
        dp[x].pop()
        res += 1
    if not dp or dp[x][-1] < y:
        dp[x].append(y)
        res +=1

print(res)



'''
                if dp[-1][1] > mel[i][1]:
        print(dp)
        while dp[-1][1] > mel[i][1]:
            res += 1
            print(dp)
            dp.pop()
            if len(dp) == 0:
                break

        '''








