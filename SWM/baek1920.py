#baekjoon 1920 find Num

def finding(target, num):
    num.sort()
    start = 0
    end = len(num) - 1

    while start <= end:
        #이진탐색은 중간값부터 값을 찾아나가기 시작한다.
        mid = (start+end)//2


        if num[mid] == target:
            return 1
        # 만약에 값이 다르면, 타겟보다 작을경우 시작숫자르
        # 타겟숫자보다 클 경우 end 숫자를 높여준다..
        elif num[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0



n = int(input())
num = list(map(int, input().split()))

case = int(input())
casenum = list(map(int, input().split()))
res = list()

for i in range(case):
    res.append(finding(casenum[i], num))

for i in range(case):
    print(res[i])