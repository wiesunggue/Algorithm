# https://www.acmicpc.net/problem/1766
# 문제집
from collections import deque
from queue import PriorityQueue
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
edge = [[] for i in range(N+1)]
table=[0]*(N+1)

for i in range(M):
    a,b = map(int,input().split())
    edge[a].append(b)
    table[b]+=1

def top_sort():
    ans = deque()
    pq = PriorityQueue()
    for i in range(1,N+1):
        if table[i]==0:
            pq.put(i)
    while pq.empty()==False:
        idx = pq.get()
        ans.append(idx)
        for i in edge[idx]:
            table[i]-=1
            if table[i]==0:
                pq.put(i)

    print(*ans)

top_sort()