n, m, v = map(int, input().split())


#인터넷을 참고해보니, index 0은 0값을 주어야 한다고 함.
matrix = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    st, en = map(int,input().split())
    matrix[st][en] = 1
    matrix[en][st] = 1


#깊이 우선 탐색
# 시작점부터, 가장 멀리 있는 정점까지 갔다오는 알고리즘
# foorprint = 한 번 들린 곳을 표시하는 것.
def dfs(current_node, row, foot_print):
    foot_print += [current_node]

    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_print:
            foot_print = dfs(search_node, row, foot_print)
    return foot_print

def bfs(start):
    st= [start]
    foot_print = [start]

    while st:
        current_node = st.pop(0)

        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_print:
                foot_print += [search_node]
                st += [search_node]
    return foot_print


print(*dfs(v, matrix, []))
print(*bfs(v))

