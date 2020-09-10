import sys
input = sys.stdin.readline
from collections import deque
import copy
import itertools

def main():
    n = int(input())
    res = list()
    for i in range(n):
        a, b = map(int, input().split())
        cnt = 0
        if a < 5:
            cnt = 0
        else:
            if a + b < 12:
                cnt = 0
            else:
                if a + b >= 12 and b < 7:
                    cnt = (a + b) // 12
                elif a + b >= 12 and b > 7:
                    tmp = b // 7
                    tmp2 = a//5
                    ans = min(tmp, tmp2)
                    na = a - 5 * ans
                    nb = b - 5 * ans
                    cnt = ans
                    if na >= 5 and (na + nb) > 12:
                        cnt += (na + nb)//12
        res.append(cnt)
    for s in res:
        print(s)
main()



''' def count(a, b):
        q = deque()
        q.append([a, b])
        cnt = 0
        while q:
            x, y = q.popleft()
            if x < 5:
                return cnt
            else:
                if x + y < 12:
                    return cnt
                else:
                    if b < 7:
                        cnt = (a + b) // 12
                        return cnt
                    else:
                        tmp = y // 7
                        tmp2 = x//5
                        ans = min(tmp, tmp2)
                        nx = x - 5 * ans
                        ny = y - 7 * ans
                        cnt += ans
                        if nx < 5:
                            return cnt
                        else:
                            q.append([nx, ny])
                            '''