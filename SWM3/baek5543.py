sum = 0
min = 2000


for i in range(3):
    n = int(input())
    if min > n:
        min = n

sum += min
min = 2000
for i in range(2):
    n = int(input())
    if min > n:
        min = n

sum += min

print(sum-50)