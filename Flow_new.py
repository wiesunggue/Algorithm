# DFS 포드-풀커슨 O((V+E)*F).=O(EF) * F는 최대 유량
# BFS 애드몬드-카프 O(V*E^2) < O(E^3)이하 일반적으로 (V<E)
import sys
INF = 10**9*2
input = sys.stdin.readline

def dfs(d, flow):
    if d == 2:
        return flow
    visit[d] = 1
    for i in range(1, N + 1):
        if arr[d][i] > 0 and visit[i] == 0:
            tmp=dfs(i, min(flow,arr[d][i]))
            if tmp!=0:
                arr[d][i] -= tmp
                arr[i][d] += tmp
                return tmp
    return 0


N, M = map(int, input().split())
visit = [0] * 201
arr = [[0 for _ in range(201)] for _ in range(201)]
ans = 0
for i in range(N):
    arr[0][i]=0
    
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1

temp = 1
while temp:
    temp = dfs(1, INF)
    visit = [0] * 401
    print(temp)
    ans += temp

print(ans)

