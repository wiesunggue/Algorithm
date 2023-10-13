# https://www.acmicpc.net/problem/2056
# 작업 문제

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
edge= [[] for i in range(N+1)]
table=[0]*(N+1)
task_time=[0]*(N+1)
ans = [0]*(N+1)
for i in range(1,N+1):
    arr = list(map(int,input().split()))
    task_time[i]=arr[0]
    for j in range(arr[1]):
        edge[arr[j+2]].append(i)
        table[i]+=1

def topo_sort():
    dq = deque()
    for i in range(1,N+1):
        if table[i]==0:
            dq.append((i,task_time[i]))
            ans[i]=task_time[i]
    while dq:
        idx,t = dq.popleft()
        ans[i]=max(ans[i],t)
        for i in edge[idx]:
            if table[i]==0:
                continue
            ans[i]=max(ans[i],task_time[i]+t)
            table[i]-=1
            if table[i]==0:
                dq.append((i,ans[i]))
    print(max(ans))

topo_sort()
