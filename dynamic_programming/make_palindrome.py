# https://www.acmicpc.net/problem/1695
# 백준 1695번 팰린드룸 만들기

N = int(input())
arr = list(map(int,input().split()))

dp = [[0]*(N+1) for i in range(N+1)]
def recur(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    add = 0 if arr[i]==arr[j] else 1
    if j-i in (0,1):
        dp[i][j] = add
        return dp[i][j]
    dp[i][j] = min(recur(i+1,j),recur(i,j-1),recur(i+1,j-1))+add
    return dp[i][j]
#recur(0,N-1)
def not_recur():
    for i in range(N-1,-1,-1):
        for j in range(i,N):
            add = int(arr[i]!=arr[j])
            minus = int(arr[i]==arr[j])
#            dp[i][j] = min(dp[i+1][j],dp[i][j-1],dp[i+1][j-1]+add)+add

            dp[i][j] = dp[i+1][j-1]+add*2
            if dp[i+1][j] == 0:
                dp[i][j] = min(dp[i][j],1)
            else:
                dp[i][j] = min(dp[i][j],dp[i+1][j]+add)
            if dp[i][j-1] == 0:
                dp[i][j] = min(dp[i][j],1)
            else:
                dp[i][j] = min(dp[i][j],dp[i][j-1]+add)
#            dp[i][j] = min(dp[i][j],dp[i+1][j]-minus+add,dp[i][j-1]-minus+add)
#            do[i][j] = min(dp[i][j],dp[i+1][j],dp[i][j-1])

not_recur()
#recur(0,N-1)
print(*dp,sep='\n')
print(dp[0][N-1])

