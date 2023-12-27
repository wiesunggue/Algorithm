# https://www.acmicpc.net/problem/30961
# 백준 30961번 최솟값, 최댓값 문제

N = int(input())
arr = sorted(map(int,input().split()))
ans = 0
for i in range(N-1):
    ans ^= arr[i]*arr[i+1]
for i in range(N):
    ans ^= arr[i]*arr[i]

print(ans)

