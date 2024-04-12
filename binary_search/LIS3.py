# https://www.acmicpc.net/problem/12738
# 백준 12738번 가장 긴 증가하는 부분 수열 3 문제

import bisect

N = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
store = [(0,arr[0])]
for i in range(N):
    if dp[-1]<arr[i]:
        dp.append(arr[i])
        store.append((len(dp)-1,arr[i]))
    else:
        k = bisect.bisect_left(dp,arr[i])
        dp[k]= arr[i]
        store.append((k,arr[i]))
print(store)
index = len(dp) - 1
result = []
for i in range(len(store)-1,-1,-1):
    if store[i][0] == index:
        result.append(store[i][1])
        index -= 1

print(result)
print(len(dp))
print(*result[::-1])