'''
백준 1977 완전제곱수

1. 완전제곱을 구하면 끝일 둣
'''

st = int(input())
end = int(input())
find = 0
min = st

for i in range(end):
    if (i*i > st) and (i*i < end):
        find = i
        min = i*i
        break
sum = 0
for i in range(find, end):
    if i*i > end:
        break
    sum += i*i

if find == 0:
    print(-1)
else:
    print(sum)
    print(min)