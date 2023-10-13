#https://www.acmicpc.net/problem/1915
# 가장 큰 정사각형 구하는 문제

n,m=map(int,input().split())
arr=[input() for i in range(n)]
cache=[[0 for _ in range(m)] for i in range(n)]
maximum=0
for i in range(n):
    if arr[i][0]=='1':
        cache[i][0]=1
        maximum=1
for i in range(m):
    if arr[0][i]=='1':
        cache[0][i]=1
        maximum=1

for i in range(1,n):
    for j in range(1,m):
        if arr[i][j]=='1':
            cache[i][j]=min(cache[i-1][j-1],cache[i][j-1],cache[i-1][j])+1
            if cache[i][j]>maximum:
                maximum=cache[i][j]
print(*cache,sep='\n')
print(maximum**2)