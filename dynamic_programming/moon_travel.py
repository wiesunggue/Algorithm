# https://www.acmicpc.net/problem/17485
# 백준 17485번 진우의 달 여행 문제
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

def dp():
    '''dp를 통한 문제 해결하기'''
    dp = [[[arr[i][j]]*3 if i==0 else [2**20]*3 for j in range(M)] for i in range(N)]
    for i in range(1,N):
        dp[i][0][1] = dp[i-1][0][0]+arr[i][0]
        dp[i][0][0] = min(dp[i-1][1][1],dp[i-1][1][2])+arr[i][0]
        dp[i][-1][1] = dp[i-1][-1][2]+arr[i][-1]
        dp[i][-1][2] = min(dp[i-1][-2][0],dp[i-1][-2][1])+arr[i][-1]
        for j in range(1,M-1):
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2])+arr[i][j]
            dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2])+arr[i][j]
            dp[i][j][2] = min(dp[i-1][j-1][0],dp[i-1][j-1][1])+arr[i][j]
    ans = 2**31
    for i in range(M):
        ans = min(ans,min(dp[-1][i]))
    print(ans)

if __name__ == '__main__':
    dp()