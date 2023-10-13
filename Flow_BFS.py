# DFS 포드-풀커슨 O((V+E)*F).=O(EF) * F는 최대 유량
# BFS 애드몬드-카프 O(V*E^2) < O(E^3)이하 일반적으로 (V<E)
import sys
from collections import deque
INF = 10**9*2
input = sys.stdin.readline

def bfs(d, end):
    dq = deque()
    dq.append(d)
    flow = INF
    visit = [0] * 10
    visit[d]=1
    
    while visit[end]==0 and dq:
        cur = dq.popleft()
        for i in range(1,N+1):
            if visit[i]==0 and arr[cur][i]:
                visit[i]=cur
                dq.append(i)
    # 경로 역추적
    if visit[end]==0:
        return 0
    i=end
    while i!=1:
        flow = min(flow, arr[visit[i]][i])
        i=visit[i]
    i=end
    while i!=1:
        arr[visit[i]][i] -= flow
        arr[i][visit[i]] += flow
        i=visit[i]
    return flow
N, M = map(int, input().split())
arr = [[0 for _ in range(401)] for _ in range(401)]
ans = 0

for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

while 1:
    tmp=bfs(1,2)
    print(tmp)
    if tmp==0:
        break
    ans+=tmp

print(ans)