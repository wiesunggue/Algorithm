# https://www.acmicpc.net/problem/21317
# 백준 21317번 징검다리 건너기 문제

N = int(input())
arr = [list(map(int,input().split())) for i in range(N-1)]
K = int(input())
ans = 2**31
for t in range(N):
    dp = [2**31]*(N+3)
    dp[0] = 0
    for i in range(N-1):
        if i in (t+1,t+2):
            continue
        if i==t:
            dp[i+3] = dp[i]+K
        else:
            dp[i+1] = min(dp[i+1],dp[i]+arr[i][0])
            dp[i+2] = min(dp[i+2],dp[i]+arr[i][1])
    ans = min(ans,dp[N-1])
    print(dp)
print(ans)