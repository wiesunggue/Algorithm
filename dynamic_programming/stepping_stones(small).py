# https://www.acmicpc.net/problem/22869
# 백준 22869번 징검다리 거넌기(small) 문제
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))

dp = [0] * (N+3)
dp[0] = 1
for i in range(N):
    for j in range(i,N):
        if dp[i]==1 and (j-i)*(1+abs(arr[i]-arr[j])) <= K:
            dp[j] = True

print('YES' if dp[N-1] else 'NO')