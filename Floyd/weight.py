# https://www.acmicpc.net/problem/10159
# 백준 10159번 저울 문제

N = int(input())
M = int(input())

graph = [[10**10 if i!=j else 0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1


for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

for i in range(1,N+1):
    cnt = 0
    for j in range(1,N+1):
        if graph[i][j]== 10**10 and graph[j][i]== 10**10:
            cnt+=1
    print(cnt)