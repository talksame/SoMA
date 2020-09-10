n = int(input())
cnt = 0
s = list(map(int, input().split()))
for i in range(5):
    if n == s[i]:
        cnt += 1

print(cnt)