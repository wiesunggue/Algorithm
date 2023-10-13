# https://www.acmicpc.net/problem/11000
# 강의실 배정 문제

import heapq
import bisect
ordered_end=[]
N=int(input())
arr=[(0,0)]*N
for i in range(N):
    a,b=map(int,input().split())
    arr[i]=(a,b)

arr.sort()
count=0
idx=0
ans=0
for i in range(N):
    start,end=arr[i]
    bisect.insort(ordered_end,end)
    while start>=ordered_end[idx]:
        idx+=1
        count-=1
    count+=1
    ans=max(ans,count)

print(ans)