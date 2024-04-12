# https://www.acmicpc.net/problem/1277
# 백준 1277번 발전소 설치 문제
import heapq,math
def dijkstra(start,N,graph):
    pq = []
    table = [10**10] * (N+1)
    table[start] = 0
    heapq.heappush(pq,(0,start))
    while pq:
        cost, idx = heapq.heappop(pq)
        for i in range(1,N+1):
            if graph[idx][i] < 10**10 and cost+graph[idx][i]<table[i]:
                table[i] = cost + graph[idx][i]
                heapq.heappush(pq,(table[i],i))

    print(int(table[N]*1000))
def dist(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
def solutions():
    N,W = map(int,input().split())
    M = float(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    graph = [[10**10]*(N+1) for i in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,i+1):
            d = dist(arr[i-1],arr[j-1])
            if d<M:
                graph[i][j] = graph[j][i] = d

    for i in range(W):
        a,b = map(int,input().split())
        graph[a][b] = 0
        graph[b][a] = 0

    dijkstra(1,N,graph)
if __name__ == '__main__':
    solutions()