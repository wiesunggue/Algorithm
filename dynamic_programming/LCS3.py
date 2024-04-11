# https://www.acmicpc.net/problem/1958
# 백준 1958번 LCS3 문제
word1 = input()
word2 = input()
word3 = input()
L1,L2,L3 = len(word1),len(word2),len(word3)
dp = [[[0 for i in range(L3+1)] for j in range(L2+1)] for k in range(L1+1)]
#dp = [[0]*(L2+1) for i in range(L1+1)]
for i in range(L1):
    for j in range(L2):
        for k in range(L3):
            if word1[i]==word2[j]==word3[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

print(dp[L1-1][L2-1][L3-1])

