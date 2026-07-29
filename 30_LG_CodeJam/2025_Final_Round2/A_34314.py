# DP 경우의 수 문제

MAX_NUMBER = 10 ** 9 + 7
T = int(input())

def solve():
    G, D = map(int, input().split())
    dp = [0] * (G+1)
    dp[0] = 1
    for i in range(G):
        for j in range(1, D+1):
            if i+j<=G:
                dp[i+j] += dp[i]
                dp[i+j] %= MAX_NUMBER

    print(dp[-1])

for t in range(T):
    solve()