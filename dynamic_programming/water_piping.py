# https://www.acmicpc.net/problem/2073
# 백준 2073번 수도배관공사 문제
import sys
input = sys.stdin.readline

D,P = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(P)]

#dp = [[2**25]*(D+1) for i in range(D+1)]
dp = [0]*(D+1)
dp[0] = 1
#dp[0] = [2**24]*(P+1)

for i in range(P):
    L, C = arr[i]
    for j in range(D,L-1,-1):
        if dp[j-L]:
            if j==L:
                dp[j] = max(dp[j],C)
            else:
                dp[j] = max(dp[j],min(dp[j-L],C))
print(dp[D])