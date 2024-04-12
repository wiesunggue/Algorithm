# https://www.acmicpc.net/problem/17396
# 백준 17396번 백도어 문제
import sys,heapq
input = sys.stdin.readline

def solutions():
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    arr[N-1] = 0
    graph = [[] for i in range(N)]
    table = [10**10]*N
    for i in range(M):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))

    start = 0
    pq = []
    heapq.heappush(pq,(0,start))
    table[start] = 0
    while pq:
        cost, idx = heapq.heappop(pq)
        if table[idx]<cost:
            continue
        for i,c in graph[idx]:
            if cost+c<table[i] and arr[i]==0:
                table[i] = cost+c
                heapq.heappush(pq,(table[i],i))

    print(table[N-1] if table[N-1]!=10**10 else -1)

if __name__ == '__main__':
    solutions()