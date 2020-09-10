'''
역시 bfs 큐로 구해보자

def bfs(matrix, n, i):
    visited = [0] * n
    q = deque()
    q.append(i)
    while q:
        idx = q.popleft()
        for i, v in enumerate(matrix[idx]):
            if visited[i] == 0 and v == 1:
                visited[i] = 1
                q.append(i)


    return visited

'''
import heapq
import sys
input = sys.stdin.readline

# 입력
V = int(input())
E = V
K = 1
INF = 100*V + 1
distance = [[] for _ in range(V+1)]  # V*V배열로 만들면 메모리가 초과된다

for _ in range(E-1):
    start, end, dist = map(int, sys.stdin.readline().split())
    distance[start].append([end, dist])  # 시작 리스트에 도착지와 거리를 입력



# 다익스트라 알고리즘
queue = []  # 우선순위 큐 -> 힙으로 구현해줌
K_distance = [INF for _ in range(V+1)]  # 답이 될 K로부터의 거리
K_distance[K] = 0  # 자기 자신은 0
heapq.heappush(queue, [0, K])  # 자기 자신으로부터 우선순위 큐를 시작한다

while queue:
    mid = heapq.heappop(queue)  # 현재 가장 가까운 거리의 노드를 pop [거리, 노드 위치]
    for end in distance[mid[1]]:  # 가장 가까운 노드에 연결된 모든 노드들 end에 대하여
        if K_distance[end[0]] > mid[0] + end[1]:  # mid노드를 거치는 게 end로 바로 가는 것보다 효율적이라면
            K_distance[end[0]] = mid[0] + end[1]  # 해당 거리를 저장
            heapq.heappush(queue, [K_distance[end[0]], end[0]])  # 큐에 [갱신된 거리, 노드 위치] 삽입


# 출력
print(K_distance)