import sys
import math
input = sys.stdin.readline

n, arr = map(int, input().split())
num = list(map(int,input().split()))
ans = math.ceil(((n-arr)/(arr-1))) + 1

print(ans)