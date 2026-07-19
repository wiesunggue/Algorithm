import sys
input = sys.stdin.readline

H, W, Q = map(int, input().split())
dp = [['A' for j in range(W)] for i in range(H)]
pri = [[0 if j!=W and i!=H else -1 for j in range(W+1)] for i in range(H+1)]
for i in range(Q):
    r, c, x = input().split()
    r, c = int(r), int(c)
    dp[r-1][c-1] = x
    pri[r-1][c-1] = i + 1
for i in range(H-1,-1,-1):
    for j in range(W-1,-1,-1):
        m = max(pri[i+1][j], pri[i][j+1], pri[i][j])
        if m == pri[i][j+1]:
            dp[i][j] = dp[i][j+1]
            pri[i][j] = pri[i][j+1]
        elif m == pri[i+1][j]:
            dp[i][j] = dp[i+1][j]
            pri[i][j] = pri[i+1][j]


ans = []
for i in range(H):
    ans.append(''.join(dp[i]))

print('\n'.join(ans))

