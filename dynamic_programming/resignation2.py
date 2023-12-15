# https://www.acmicpc.net/problem/15486
# 백준 15486번 퇴사 2 문제
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

dp = [0] * (N+60)
for i in range(N):
    dp[i+1] = max(dp[i+1],dp[i])
    dp[i+arr[i][0]] = max(dp[i+arr[i][0]],dp[i]+arr[i][1])

print(dp[N])