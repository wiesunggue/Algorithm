# https://www.acmicpc.net/problem/2758
# 백준 2758번 로또 문제
def solution():
    N, M = map(int, input().split())

    # 절대로 로또를 구매하지 못하는 경우
    if 2**(N-1)>M:
        return 0

    dp = [[0]*(M+1) for i in range(N+1)] #dp[N][M]
    for i in range(M+1):
        dp[1][i] = 1
    for i in range(2,N+1):
        for j in range(1,M+1):
#            for k in range(j//2+1):
#                print(i,j,k)
#                dp[i][j] += dp[i-1][k]
            if j%2==0:
                dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
            else:
                dp[i][j] = dp[i][j-1]
    print(*dp,sep='\n')
    return sum(dp[N])

T = int(input())

for test in range(T):
    print(solution())