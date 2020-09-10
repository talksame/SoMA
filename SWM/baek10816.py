#baekjoon 10816 counting card
import sys


n = map(int, sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

res = {}

#사전형 자료형에 동일한 원소가 있을 경우 그 원소의 값을 +1 해준다.
for i in card:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1

m = map(int, sys.stdin.readline())
cardcase = list(map(int, sys.stdin.readline().split()))

for s in cardcase:
    #해당 숫자가 결과 딕셔너리에 있을 경우 그 value 값을 출력해준다.
    if s in res:
        #숫자와 띄어쓰기를 더할 순 없으니, 문자로 변환해준다.
        sys.stdout.write(str(res[s]) + " ")
    else:
        #없을 경우에는 0을 출력!
        sys.stdout.write('0 ')
