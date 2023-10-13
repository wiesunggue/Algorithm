# https://www.acmicpc.net/problem/1092
# 배 문제

N=int(input())
arr=list(map(int,input().split()))
M=int(input())
box=list(map(int,input().split()))
arr.sort()
box.sort()
box_arr=[0 for i in range(N)]
idx=0
for i in range(N):
    while idx<M and arr[i]>=box[idx]:
        box_arr[i]+=1
        idx+=1
box_arr.reverse()
m=0

for i in range(N):
    m=max((sum(box_arr[:i+1])+i)//(i+1),m)
print(-1 if arr[-1]<box[-1] else m)