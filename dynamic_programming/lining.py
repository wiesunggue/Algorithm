# https://www.acmicpc.net/problem/2631
# 백준 2631번 줄세우기 문제

N = int(input())
arr = [int(input()) for i in range(N)]
dp = [0]*N
print(arr)
def lis():
    for i in range(N):
        dp[i] = 1
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[i],dp[j]+1)
lis()
print(dp)
print(N-max(dp))

