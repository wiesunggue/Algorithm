import sys
import heapq

INF = 2 ** 30
rinput = sys.stdin.readline
rprint = sys.stdout.write


def dijkstra(src):
    dist = [INF for i in range(N + 1)]
    dist[src] = 0
    pq = []
    heapq.heappush(pq, (0, src)) # 시작점 : src
    while pq:
        cost, here = heapq.heappop(pq)
        cost = -cost
        if dist[here] < cost:
            continue
        for i in adj[here]:
            there = i[0]
            nextDist = cost + i[1]
            if dist[there] > nextDist:
                dist[there] = nextDist
                heapq.heappush(pq, (-nextDist, there))
    
    return dist

N = int(rinput())
M = int(rinput())
adj = [[] for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, rinput().split())
    adj[a].append((b, c))
fr, to = map(int, rinput().split())
cost = dijkstra(fr)[to]
print(cost)
