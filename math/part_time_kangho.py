# https://www.acmicpc.net/problem/1758
# 백준 1758번 알바생 강호
N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort(reverse=True)
ans = 0
for i in range(N):
    ans += max(0,arr[i]-i)

print(ans)