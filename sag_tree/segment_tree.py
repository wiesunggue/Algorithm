from math import log2
import sys
sys.setrecursionlimit(10**5)
rinput = sys.stdin.readline
rprint = sys.stdout.write
n = int(input())
dp=[[0 for i in range(n)] for i in range(n)]
s = [list(map(int,input().split())) for i in range(n)]

for i in range(1,n):
    for j in range(n-i):
        x = j+i
        dp[j][x]=2**32
        for k in range(j,x):
            if j==0 and x==3:
                print(j,k, k+1,x)
            dp[j][x] = min(dp[j][x],dp[j][k]+dp[k+1][x]+s[j][0]*s[k][1]*s[x][1])


print(*dp,sep='\n')