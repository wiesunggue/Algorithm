# https://www.acmicpc.net/problem/17835
# 면접보는 승범이네
import heapq
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
city = [[] for i in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    city[b].append((a,c))

arr = list(map(int,input().split()))

def dijkstra():
    table = [10**10] * (N+1)
    priority_queue = []
    for i in range(K):
        table[arr[i]] = 0
        heapq.heappush(priority_queue,(0,arr[i]))
    while priority_queue:
        score,n = heapq.heappop(priority_queue)
        if table[n]< score:
            continue
        for c,s in city[n]:
            new_score = score + s
            if new_score>=table[c]:
                continue
            table[c] = new_score
            heapq.heappush(priority_queue,(new_score,c))
    print(table.index(max(table[1:])))
    print(max(table[1:]))
dijkstra()
