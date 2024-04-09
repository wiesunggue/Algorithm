# https://www.acmicpc.net/problem/15989
# 백준 15989번 1, 2, 3 더하기 4 문제

N = int(input())
arr = [int(input()) for i in range(N)]
dp = [[0]*4 for i in range(max(arr)+10)]
dp[0] = [1]*4
for i in range(1,len(dp)):
    #if i>=3:
    dp[i][3] = dp[i-1][1]+dp[i-2][2]+dp[i-3][3]
    #if i>=2:
    dp[i][2] = dp[i-1][1]+dp[i-2][2]
    dp[i][1] = dp[i-1][1]

print(*dp,sep='\n')
for i in arr:
    print(dp[i][3])
