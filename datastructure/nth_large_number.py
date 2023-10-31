# https://www.acmicpc.net/problem/2075
# 백준 2075번 N번째 큰 수
import heapq

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
pq = []
for i in range(N):
    heapq.heappush(pq,(-arr[-1][i],i,-1))

for i in range(N-1):
    _,x,y = heapq.heappop(pq)
    print(_)
    heapq.heappush(pq,(-arr[y-1][x],x,y-1))

print(-heapq.heappop(pq)[0])