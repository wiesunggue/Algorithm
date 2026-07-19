import sys
input = sys.stdin.readline

T = int(input())
for test in range(T):
    N = int(input())
    S = input()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    dp = [[0, 0] for i in range(N)]
    if S[0] == "S":
        dp[0][1] = -X[0]
    else:
        dp[0][0] = -X[0]
    for i in range(1, N):
        if S[i] == 'S':
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + Y[i-1])
            dp[i][1] = max(dp[i-1][0], dp[i-1][1]) - X[i]
        else:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + Y[i-1]) - X[i]
            dp[i][1] = max(dp[i-1][0], dp[i-1][1])

    print(max(dp[N-1]))