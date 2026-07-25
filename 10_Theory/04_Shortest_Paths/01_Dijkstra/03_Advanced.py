# 1	2325	개코전쟁	Platinum V	최단경로 복원 → 경로 간선을 하나씩 제거 → 다익스트라 반복	★★★★★
# 2	1854	K번째 최단경로 찾기	Platinum IV	정점마다 최단거리 하나가 아니라 상위 K개 유지	★★★★★
import heapq
N, M, K = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    pq = []
    table = [[] for i in range(N+1)]

    heapq.heappush(pq, (0, start))
    heapq.heappush(table[start], 0)

    while pq:
        cost, node = heapq.heappop(pq)
        if len(table[node]) == K and cost > -table[node][0]:
            continue

        for n, c in graph[node]:
            if len(table[n]) < K:
                heapq.heappush(table[n], -cost - c)
                heapq.heappush(pq, (cost + c, n))
            elif cost + c < - table[n][0]:
                heapq.heappop(table[n])
                heapq.heappush(table[n], -cost - c)
                heapq.heappush(pq, (cost + c, n))
    return table

table = dijkstra(1)
for i in range(1, N+1):
    print(-table[i][0] if len(table[i])==K else -1)

# 3	22870	산책 (large)	Platinum IV	최단거리 구조를 이용한 사전순 경로 복원 + 정점 제거	★★★★★
# 4	13907	세금	Platinum IV	dist[정점][사용 간선 수] + 간선 비용 일괄 증가 질의	★★★★★
# 5	10217	KCM Travel	Platinum IV	비용 제한이 있는 상태 확장 최단경로 + 지배 상태 제거	