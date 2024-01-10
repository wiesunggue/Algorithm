# https://www.acmicpc.net/problem/20542
# 백준 20542번 받아쓰기 문제

N,M = map(int,input().split())
myAns = input()
solution = input()
dp = [[0]*(M+1) for i in range(N+1)]

# LCS 구하기
for i in range(1,N+1):
    for j in range(1,M+1):
        if myAns[i-1]==solution[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        elif (myAns[i-1]=='v' and solution[j-1]=='w') or (myAns[i-1]=='i' and solution[j-1] in ['j','l']):
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# 1개라도 공통 수열이 존재하는 경우
if dp[N][M]!=0:
    i,j = N,M
    ansIdx = []
    solIdx = []
    ## LCS 역추적
    while (i!=0 and j!=0):
        print(i,j)
        if dp[i-1][j]==dp[i][j]:
            i -= 1
        elif dp[i][j-1]==dp[i][j]:
            j -= 1
        elif dp[i-1][j-1] < dp[i][j]:
            ansIdx.append(i - 1)
            solIdx.append(j-1)
            i -= 1
            j -= 1

    ansIdx.reverse()
    solIdx.reverse()
    print(ansIdx,solIdx)
    answer = max(ansIdx[0],solIdx[0])
    for i in range(1,dp[N][M]):
        print(i)
        answer += max(ansIdx[i]-ansIdx[i-1]-1,solIdx[i]-solIdx[i-1]-1)
    answer += max(N-ansIdx[-1],M-solIdx[-1])-1
else: # 겹치는게 하나도 없는 경우
    answer = max(N,M)
print(answer)
