# https://www.acmicpc.net/problem/11508
# 백준 11508번 2+1 세일 문제

N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort(reverse=True)
ans = 0
cnt = 0
for i in range(N//3*3):
    cnt += 1
    cnt %= 3
    if cnt == 0:
        continue
    ans += arr[i]

ans += sum(arr[N//3*3:])
print(ans)