import sys
input = sys.stdin.readline


def main():
    n = int(input())
    res = list()
    for i in range(n):
        a, b = map(int, input().split())
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
        res.append(count(a,b))
    for s in res:
        print(s)