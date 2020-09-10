'''
baek 18232 텔레포트

1. DP로 풀어나간다.
2. min 값을 찾는다.

'''



from _collections import deque

def bfs(adj, v):
    Q = deque([v])
    dist = [-1]




