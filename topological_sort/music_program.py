# https://www.acmicpc.net/problem/2623
# 음악 프로그램

import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
edge = [[]for i in range(N+1)]
table=[0]*(N+1)

for i in range(M):
    arr=list(map(int,input().split()))[1:]
    for j in range(1,len(arr)):
        edge[arr[j-1]].append(arr[j])
        table[arr[j]]+=1

def topological_sort():
    ans = deque()
    dq = deque()
    for i in range(1,N+1):
        if table[i]==0:
            dq.append(i)

    while dq:
        idx = dq.popleft()
        ans.append(idx)
        for i in edge[idx]:
            if table[i]==0:
                continue
            table[i]-=1
            if table[i]==0:
                dq.append(i)
    print(table)
    if len(ans)!=N:
        print(0)
    else:
        print(*ans,sep='\n')
topological_sort()