# https://www.acmicpc.net/problem/1106
# 호텔
MAX_COST=100001
C,N=map(int,input().split())
city_cost=[(list(map(int,input().split())))for i in range(N)]
dp=[0]*MAX_COST
cost=0
for i in range(MAX_COST):
    for j in range(N):
        a,b=city_cost[j]
        if i-a>=0:
            dp[i]=max(dp[i],dp[i-a]+b)
    if dp[i]>=C:
        cost=i
        break

print(cost)