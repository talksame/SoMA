'''
백준 11724 연결요소의 개수

'''

from _collections import deque


spot, line = map(int, input().split())
matrix = [[0]*(spot+1) for _ in range(spot+1)]
dp = [0] * (spot+1)
for s in range(line):
    st, ed = map(int, input().split())
    matrix[st][ed] = 1
    matrix[ed][st] = 1

def bfs(node):
    q = [node]

    foot_print = [node]

    while q:
        cur_node = q.pop(0)

        for search in range(len(matrix[cur_node])):
            if matrix[cur_node][search] and search not in foot_print:
                foot_print += [search]
                q += [search]

    return sorted(foot_print)

res = list()
for i in range(1, spot+1):
    temp = bfs(i)
    if temp not in res:
        res.append(temp)

print(len(res))