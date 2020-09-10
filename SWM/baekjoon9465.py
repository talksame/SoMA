#baekjoon 스티커

'''
스티커가 지워지지 않는 부분의 인덱스를 생각한다.
규칙을 찾아야 한다.

'''


case = int(input())
ans = list()
for k in range(case):
    sti = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    res = [line1, line2]
    res[0][1] += res[1][0]
    res[1][1] += res[0][0]
    for i in range(2, sti):
        res[0][i] += max(res[1][i-2], res[1][i-1])
        res[1][i] += max(res[0][i-2], res[0][i-1])
    ans.append(max(res[0][sti-1], res[1][sti-1]))

for i in range(case):
    print(ans[i])

