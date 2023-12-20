# https://www.acmicpc.net/problem/2624
# 백준 2624번 동전 바꿔주기 문제

T = int(input())
K = int(input())
coins = [list(map(int,input().split())) for i in range(K)]
coins.sort()

ans = [0] * (T+10)
ans[0] = 1

for i in range(K):
    for j in range(T-coins[i][0],-1,-1):
        if ans[j] == 0: continue;
        for k in range(1,coins[i][1]+1):
            if j+coins[i][0]*k > T: break;
            ans[j+coins[i][0]*k] += ans[j]

print(ans[T])

