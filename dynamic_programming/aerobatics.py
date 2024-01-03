# https://www.acmicpc.net/problem/21923
# 백준 21923번 곡예 비행 문제

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
dp = [[[0]*2 for j in range(M)] for i in range(N)]

for j in range(M):
    for i in range(N-1,-1,-1):
        if i==N-1 and j==0:
            dp[i][j][0] = arr[i][j]
        elif j==0:
            dp[i][j][0]=dp[i+1][j][0]+arr[i][j]
        elif i==N-1:
            dp[i][j][0]=dp[i][j-1][0]+arr[i][j]
        else:
            dp[i][j][0] = max(dp[i+1][j][0],dp[i][j-1][0])+arr[i][j]


for j in range(M-1,-1,-1):
    for i in range(N-1,-1,-1):
        if i==N-1 and j==M-1:
            dp[i][j][1] = arr[i][j]
        elif i==N-1:
            dp[i][j][1]=dp[i][j+1][1]+arr[i][j]
        elif j==M-1:
            dp[i][j][1]=dp[i+1][j][1]+arr[i][j]
        else:
            dp[i][j][1] = max(dp[i+1][j][1],dp[i][j+1][1])+arr[i][j]

ans = -10**20
for i in range(N):
    for j in range(M):
        ans = max(ans,dp[i][j][0]+dp[i][j][1])

print(*dp,sep='\n')
print(ans)
