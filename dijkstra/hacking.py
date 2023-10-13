# https://www.acmicpc.net/problem/10282
# 해킹 문제

from queue import PriorityQueue
import sys
input = sys.stdin.readline
T = int(input())

def dijkstra():
    n,d,c = map(int,input().split())
    node=[[]for i in range(n+1)]
    table=[10**9]*(n+1)
    visit=[0]*(n+1)
    for i in range(d):
        a,b,s=map(int,input().split())
        node[b].append((a,s))
    pq = PriorityQueue()
    pq.put((0,c))
    table[c]=0
    while pq.empty()==False:
        score,idx=pq.get()
        if visit[idx]!=0:
            continue
        visit[idx]=1
        for i,s in node[idx]:
            table[i]=min(table[i],table[idx]+s)
            pq.put((table[i],i))

    m=0
    cnt=0
    for i in range(len(table)):
        if table[i]<10**9:
            m=max(table[i],m)
            cnt+=1
    print(cnt,m)

for test in range(T):
    dijkstra()
