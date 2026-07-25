# 최단 경로 찾기 알고리즘 Dijkstra
import heapq
N = 10**5
graph = []
# graph append 완료 가정

def dijkstra():
    pq = []
    visit = [False] * (N + 1) # visit의 정확한 의미는 방문 여부가 아닌 최단거리 보장 여부를 검토하는 기능임
    table = [float('inf')] * (N + 1)

    heapq.heappush(pq, (0, 1))  # 시작점은 1번 노드
    table[1] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visit[node]:
            continue
        visit[node] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx]:
                table[idx] = cost + weight
                heapq.heappush(pq, (table[idx], idx))

# 한번 확정된 노드는 다시 업데이트 할 필요없음
# 모든 가중치가 0 이상이므로, PQ에서 가장 적은 비용으로 꺼낸 노드에 대해 나중에 더 짧은 경로가 나타날 수 없음

# 기본 문제 : 1753 최단 경로
import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[] for i in range(V+1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    visit = [False] * (V + 1)
    table = [float('inf')] * (V + 1)
    table[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visit[node]:
            continue
        visit[node] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx]:
                table[idx] = cost + weight
                heapq.heappush(pq, (table[idx], idx))

    return table

table = dijkstra(K)
for i in range(1, V + 1):
    print(table[i] if table[i] != float('inf') else "INF")

# 심화 문제 : 1504 특정한 최단 경로
# 다익스트라 도중 임의의 두 노드를 거쳐서 1->N으로 가는 최단 경로를 구하는 문제
# case 1 : 1 -> v1 -> v2 -> N
# case 2 : 1 -> v2 -> v1 -> N
# 두 가지 경로 중 더 짧은 경로를 선택하면 됨
import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    visit = [False] * (N + 1)
    table = [float('inf')] * (N + 1)
    table[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visit[node]:
            continue
        visit[node] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx]:
                table[idx] = cost + weight
                heapq.heappush(pq, (table[idx], idx))

    return table

case1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
case2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]

answer = min(case1, case2)
if answer >= float('inf'):
    print(-1)
else:
    print(answer)


# 응용 문제 : 9370 미확인 도착지
# 항상 최단거리로 이동하고, 시작점s, g-h 사이의 간선을 통과할 때 목적지를 찾기 문제
# 그럼 s->g->h->x or s->h->g->x 인 경로를 찾으면 되는거 아닌가?
# case1, case2의 결과에 대해 min(case1, case2)를 모두 비교하고 최솟값을 모두 찾으면 됨
# 즉 1504 문제와 동치이다.

