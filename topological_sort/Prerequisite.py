# https://www.acmicpc.net/problem/14567
# 선수 과목 문제
import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
table = [0]*(N+1)
ans = [0]*(N+1)
edge=[[]for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    table[b]+=1
    edge[a].append(b)

def topological_sort():
    dq=deque()
    semester = 1
    for i in range(1,N+1):
        if table[i]==0:
            dq.append(i)
            ans[i]=semester
    semester+=1
    dq.append(-1)
    while dq:
        idx = dq.popleft()
        print(idx)
        if idx==-1 and dq:
            semester+=1
            dq.append(-1)
            continue
        for i in edge[idx]:
            table[i]-=1
            ans[i]=semester
            if table[i]==0:
                dq.append(i)
    print(*ans[1:])
topological_sort()