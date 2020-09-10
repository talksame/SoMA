#baekjoon 1026

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += max(b)*min(a)
    a.remove(min(a))
    b.remove(max(b))

print(sum)