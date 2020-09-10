#baek 1773
import sys
stu, time = map(int,sys.stdin.readline().split())
check = [0]*(time + 1)


cnt = 0

for i in range(stu):
    n = int(sys.stdin.readline())
    for j in range(n, time+1, n):
        if check[j] == 0:
            check[j] =1
            cnt +=1

sys.stdout.write(str(cnt))

