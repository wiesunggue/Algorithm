# https://www.acmicpc.net/problem/1823
# 백준 1823번 수확 문제
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
dp = [[-1 for j in range(N+1)] for i in range(N+1)]

for i in range(N+1):
    for j in range(N,i-1,-1):
        if i==0 and j==N:
            dp[i][j] = 0
        elif j==N:
                dp[i][j] = dp[i-1][N]+arr[i-1]*i
        elif i==0:
                dp[i][j] = dp[i][j+1]+arr[j]*(N-j)
        else:
            dp[i][j] = max(dp[i-1][j]+arr[i-1]*(N-j+i),dp[i][j+1]+arr[j]*(N-j+i))

print(max([dp[i][i] for i in range(N+1)]))