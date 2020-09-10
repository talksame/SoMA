'''
히스토그램의 최대 넓이 구하기
'''



res = list()

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    real = a[1:] + [0]
    dp = []
    max = 0
    for i, value in enumerate(real):
        while dp and real[dp[-1]] > value:
            h = real[dp.pop()]
            if dp:
                w = i - dp[-1] -1
            else:
                w = i
            if h * w > max:
                max = h * w
        dp.append(i)
    res.append(max)

for i in res:
    print(i)
