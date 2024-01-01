# https://www.acmicpc.net/problem/1695
# 백준 1695번 팰린드룸 만들기

N=int(input())
arr=list(map(int,input().split()))
dp=[[0]*(N+1) for i in range(N+1)]
for i in range(N-1,-1,-1):
    for j in range(i+1,N):dp[i][j]=dp[i+1][j-1]if arr[i]==arr[j]else min(dp[i+1][j],dp[i][j-1])+1
print(dp[0][N-1])