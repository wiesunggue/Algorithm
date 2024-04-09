# https://www.acmicpc.net/problem/13424
# 백준 13424번 비밀 모임 문제
from copy import deepcopy
import heapq

def solutions():
    '''플로이드 워셜 방법'''
    N,M = map(int,input().split())
    node = [[10**10 if i!=j else 0 for j in range(N+1)] for i in range(N+1)]
    dist = deepcopy(node)
    for i in range(M):
        a,b,c = map(int,input().split())
        node[a][b] = node[b][a] = c
        dist[a][b] = dist[b][a] = c
    K = int(input())
    arr = list(map(int,input().split()))

    # 최단 거리 계산하기
    for i in range(1,N+1):
        for j in range(1,N+1):
            for k in range(1,N+1):
                dist[j][k] = min(dist[j][k],dist[j][i]+dist[i][k])
    ans_sum = 10**10

    # 친구로 부터 거리 계산하기
    for i in range(1,N+1):
        mid_sum = 0
        for j in arr:
            mid_sum += dist[i][j]
        if mid_sum<ans_sum:
            ans_sum = mid_sum
            ans_pos = i
    print(*dist,sep='\n')
    print(ans_pos)

def dijkstra(graph,start,N):
    pq = []
    table = [10**10]*(N+1)
    table[start] = 0
    heapq.heappush(pq,(0,start))
    while pq:
        dist, idx = heapq.heappop(pq)
        if table[idx]<dist:
            continue
        for i,d in graph[idx]:
            if dist+d < table[i]:
                table[i] = dist+d
                heapq.heappush(pq,(table[i],i))
    print(table)
    return table
def solutions():
    '''다익스트라 방법'''
    N,M = map(int,input().split())
    graph = [[] for i in range(N+1)]
    table = [[10**10]*(N+1) for i in range(N+1)]
    # 그래프 만들기
    for i in range(M):
        a,b,c = map(int,input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])

    K = int(input())
    arr = list(map(int,input().split()))
    for i in arr:
        table[i] = dijkstra(graph,i,N)

    # 친구로 부터 거리 계산하기
    ans_sum = 10**10
    for i in range(1,N+1):
        mid_sum = 0
        for j in arr:
            mid_sum += table[j][i]
        if mid_sum<ans_sum:
            ans_sum = mid_sum
            ans_pos = i

    print(ans_pos,ans_sum)
if '__main__' == __name__:
    T = int(input())
    for test in range(T):
        solutions()