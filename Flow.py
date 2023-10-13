# DFS 포드-풀커슨 O((V+E)*F).=O(EF) * F는 최대 유량
# BFS 애드몬드-카프 O(V*E^2) < O(E^3)이하 일반적으로 (V<E)
# 최대유량(E^3) -> 이분 매칭(VE)을 느리게 해결 가능하다.
import sys
input=sys.stdin.readline

def dfs(d):
    if d == 2:
        return 1
    visit[d] = 1
    for i in range(1, N + 1):
        if arr[d][i]>0 and visit[i] == 0:
            if dfs(i):
                arr[d][i] -= 1
                arr[i][d] += 1
                return 1
    return 0

N,M=map(int,input().split())
visit=[0]*401
arr=[[0 for _ in range(401)] for _ in range(401)]
ans=0
for i in range(M):
    a,b=map(int,input().split())
    arr[a][b]=1
    
temp=1
while temp:
    temp=dfs(1)
    visit=[0]*401
    ans+=temp
    
print(ans)

