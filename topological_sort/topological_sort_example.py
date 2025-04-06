import time
import sys
input = sys.stdin.readline
print = sys.stdout.write

def dfs(here):
    visit[here] = 1
    for there in graph[here]:
        if visit[there] == -1:
            dfs(there)
    order.append(str(here+1))

def topologicalSort():
    for here in range(N):
        if visit[here] == -1:
            dfs(here)

    order.reverse()
    print(" ".join(order))

N, M = map(int,input().split())
graph = [[] for i in range(N)]
visit = [-1] * N
order = []

for i in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
topologicalSort()