# https://www.acmicpc.net/problem/16938
# 캠프 준비 문제

N,L,R,X = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
subset = (1<<N)-1
removed = subset
cnt=0

while subset:
    Min = 10 ** 10
    Max = 0
    total = 0
    for i in range(N):
        if subset & (1<<i):
            Min = min(Min,arr[i])
            Max = max(Max,arr[i])
            total += arr[i]
    if total>=L and total<=R and (Max-Min)>=X:
        cnt+=1
    subset = (subset-1) & removed

print(cnt)