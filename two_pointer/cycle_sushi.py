# https://www.acmicpc.net/problem/2531
# 백준 2531번 회전 초밥

N,d,k,c = map(int,input().split())
arr = [int(input()) for i in range(N)]

sushi = [0]*(d+1)
cnt = 0
ans = 0
for i in range(k):
    sushi[arr[-i-1]]+=1
    if sushi[arr[-i-1]]==1:
        cnt+=1
print(sushi)
for i in range(N):
    sushi[arr[i]]+=1
    cnt += sushi[arr[i]]==1
    sushi[arr[i-k]]-=1
    cnt -= sushi[arr[i-k]]==0
    print(sushi,cnt)
    ans = max(cnt+1 if sushi[c]==0 else cnt,ans)
print(ans)