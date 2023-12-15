# https://www.acmicpc.net/problem/22857
# 백준 22857번 가장 긴 짝수 연속한 부분 수열 (small) 문제

N,K = map(int,input().split())
arr = list(map(int,input().split()))

ans = []
cnt = 0
for i in range(N):
    if arr[i]%2==1:
        ans.append(cnt)
        cnt = 0
    else:
        cnt += 1

ans.append(cnt)
print(ans)
total = sum(ans[0:K+1])
answer = total
print(total)
for i in range(len(ans)-K-1):
    total = total-ans[i]+ans[i+K+1]
    print(total,i,i+K+1)
    answer = max(total,answer)
print(total)