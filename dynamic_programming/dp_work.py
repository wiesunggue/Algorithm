#https://www.acmicpc.net/problem/14430
# 자원 캐기

N,M=map(int,input().split())
arr=[list(map(int,input().split()))for i in range(N)]
cache=[[0 for i in range(M)]for j in range(N)]
for i in range(N):
    for j in range(M):
        if i==0:
            cache[i][j]=cache[i][j-1]+arr[i][j]
        elif j==0:
            cache[i][j]=cache[i-1][j]+arr[i][j]
        else:
            cache[i][j]=max(cache[i][j-1]+arr[i][j],cache[i-1][j]+arr[i][j])

print(*cache,sep='\n')
#print(cache[N-1][M-1])