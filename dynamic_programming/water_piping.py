# https://www.acmicpc.net/problem/2073
# 백준 2073번 수도배관공사 문제
import sys
input = sys.stdin.readline

D,P = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(P)]

dp = [[2**25]*(P+1) for i in range(D+1)]
dp[0] = [2**24]*(P+1)

for i in range(1,D+1):
    for j in range(P):
            L, C = arr[j]
            if i-L>=0:
                dp[i][j] = min(dp[i-L][j-1],C)
print(*dp,sep='\n')
print(dp[D][P])
