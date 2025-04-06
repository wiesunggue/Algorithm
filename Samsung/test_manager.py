# https://www.acmicpc.net/problem/13458
N = int(input())
arr = list(map(int,input().split()))
B,C = map(int,input().split())
ans = 0
for i in arr:
    ans += max(0,i-B+C-1)//C + 1

print(ans)