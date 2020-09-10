
a = int(input())
cow = list()

for i in range(a):
    cow.append(int(input()))

dp = [0 for i in range(a)]
sum = 0
for i in range(a):
    left = cow[i]
    right =

