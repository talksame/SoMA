
def empty(a):
    if len(a) == 0:
        return True
    else:
        return False

case = int(input())
num = list()
dp = list()
res = list()
b = [ i for i in range(case, 0, -1)]
for i in range(case):
    num.append(int(input()))

for i in range(case):
    while True:
        if not dp:
            dp.append(b.pop())
            res.append('+')
        elif dp[-1] == num[i]:
            dp.pop()
            res.append('-')
            break
        elif not b:
            break
        else:
            dp.append(b.pop())
            res.append('+')

if not empty(dp):
    print('NO')
else:
    for i in res:
        print(i)