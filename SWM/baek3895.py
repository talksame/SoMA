#baek 3895 남은 돌 치우기


res = list()

cnt = 0
n, k, m = map(int, input().split())

stone = [ i + 1 for i in range(n)]

check = 0
while len(stone) > 1 :
    print(stone)
    if check == 0:
        m = 3
        check =1
    elif check == 1:
        m = m + k
        check = 0

    if m >= len(stone):
        m = m - len(stone)

    del stone[m-1]




