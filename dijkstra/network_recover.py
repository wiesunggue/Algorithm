# https://www.acmicpc.net/problem/2211
# 네트워크 복구 문제
from queue import PriorityQueue
import sys
input = sys.stdin.readline
def dijkstra():
    N,M = map(int,input().split())
    node = [[]for i in range(N+1)]
    for i in range(M):
        a,b,c=map(int,input().split())
        node[a].append((b,c))
        node[b].append((a,c))
    visit=[0]*(N+1)
    table=[[10**9,[]]for i in range(N+1)]
    table[1]=0,[]
    pq = PriorityQueue()
    pq.put((0,1,[]))
    while pq.empty()==False:
        score,idx,lis = pq.get()
        if visit[idx]!=0:
            continue
        visit[idx]=1
        for i,s in node[idx]:
            if table[i][0]>s+table[idx][0]:
                table[i][0]=s+table[idx][0]
                table[i][1]=lis+[idx]
            pq.put((table[i][0],i,table[i][1]))
    set_ans = set()
    for i in range(N+1):
        if table[i][1]==[]:
            continue
        for j in range(len(table[i][1])-1):
            set_ans.add((min(table[i][1][j],table[i][1][j+1]),max(table[i][1][j],table[i][1][j+1])))
        print(table[i])
        set_ans.add((min(table[i][1][-1],i),max(table[i][1][-1],i)))
    print(len(set_ans))
    for i in set_ans:
        print(*i)
dijkstra()