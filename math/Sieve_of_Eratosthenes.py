# https://www.acmicpc.net/problem/2960
# 백준 2960번 에라토스테네스의 체 문제

N,K = map(int,input().split())
arr = [1 for i in range(N+1)]
ans = [0 for i in range(N+1)]
cnt = 0
for i in range(2,N+1):
    if arr[i] != 0:
        arr[i] = 0
        cnt += 1
        ans[i] = cnt
        for j in range(2,1000):
            if i*j<=N:
                if arr[i*j] != 0:
                    arr[i*j] = 0
                    cnt += 1
                    ans[i*j] = cnt

print(ans.index(K))