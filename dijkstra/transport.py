# https://www.acmicpc.net/problem/5972
# 백준 5972번 택배 배송 문제
import heapq

N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
table = [10**10]*(N+1)
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra():
    pq = []
    start = 1
    heapq.heappush(pq,(0,start))
    table[start] = 0

    while pq:
        cost, idx = heapq.heappop(pq)
        for next_idx,c in graph[idx]:
            if cost+c<table[next_idx]:
                table[next_idx]= cost+c
                heapq.heappush(pq,(table[next_idx],next_idx))

    print(table)

dijkstra()