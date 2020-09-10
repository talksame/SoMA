#baekjoon 1773 Fibo_extend

n = int(input())

res = [0, 1]

for i in range(2, abs(n) + 1):
    temp = (res[i - 2] + res[i-1])%1000000000
    res.append(temp)

if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(res[abs(n)])