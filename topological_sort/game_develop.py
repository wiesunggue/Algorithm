# https://www.acmicpc.net/problem/1516
# 게임 개발

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
edge = [[]for i in range(N+1)]
table=[0]*(N+1)
build_time=[0]*(N+1)
ans_time=[0]*(N+1)

for i in range(1,N+1):
    arr=list(map(int,input().split()))
    build_time[i]=arr[0]
    for j in range(1,len(arr)-1):
        edge[arr[j]].append(i)
        table[i]+=1
print(table)
def topo_sort():
    dq = deque()
    for i in range(1,N+1):
        if table[i]==0:
            dq.append((i,build_time[i]))
            ans_time[i]=build_time[i]
    while dq:
        idx,used_time = dq.popleft()
        for i in edge[idx]:
            if table[i]==0:
                continue
            table[i]-=1
            ans_time[i] = max(ans_time[i], used_time + build_time[i])
            if table[i]==0:
                dq.append((i,ans_time[i]))

    print(*ans_time[1:],sep='\n')

topo_sort()