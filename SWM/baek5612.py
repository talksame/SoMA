#baekjoon 5612

time = int(input())
car = int(input())

max = car

for i in range(time):
    a, b= map(int, input().split())
    car = car + a - b
    if car > max:
        max = car
    if car < 0:
        max = 0
        break
print(max)