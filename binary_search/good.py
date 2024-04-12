# https://www.acmicpc.net/problem/1253
# 백준 1253번 좋다 문제

import bisect
N = int(input())
arr = sorted(list(map(int,input().split())))


ans = [0]*N
for i in range(N):
    for j in range(N):
        if ans[i]==1 or i==j:
            continue
        left = bisect.bisect_left(arr,arr[i]-arr[j])
        right = bisect.bisect_right(arr,arr[i]-arr[j])
        if right-left == 1 and j!=left and i!=left:
            ans[i] = 1
        if right-left == 2 and not ((left+1==i and left==j) or (left+1==j and left==i)):
            ans[i] = 1
        elif right-left > 2:
            ans[i] = 1
print(sum(ans))