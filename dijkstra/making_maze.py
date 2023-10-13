# https://www.acmicpc.net/problem/2665
# 미로 만들기

from queue import PriorityQueue
import sys
input = sys.stdin.readline
N = int(input())

def dijkstra(start,end):
    table=[[10**9for i in range(N)]for j in range(N)]
    visit=[[0for i in range(N)]for j in range(N)]
    sx,sy=start
    ex,ey=end
    table[sx][sy]=0
    zero_one=lambda x: 0 if x=='1' else 1
    arr = [list(map(zero_one,list(input().rstrip()))) for i in range(N)]
    pq = PriorityQueue()
    pq.put((0,*start))
    while pq.empty()==False:
        score,px,py=pq.get()
        print(px,py)
        if visit[px][py]!=0:
            continue
        visit[px][py]=1
        if px-1>=0:
            table[px-1][py]=min(table[px-1][py],arr[px-1][py]+score)
            pq.put((table[px-1][py],px-1,py))
        if py-1>=0:
            table[px][py-1]=min(table[px][py-1],arr[px][py-1]+score)
            pq.put((table[px][py-1],px,py-1))
        if px+1<N:
            table[px+1][py]=min(table[px+1][py],arr[px+1][py]+score)
            pq.put((table[px+1][py],px+1,py))
        if py+1<N:
            table[px][py+1]=min(table[px][py+1],arr[px][py+1]+score)
            pq.put((table[px][py+1],px,py+1))
    print(*table,sep='\n')
    return table[ex][ey]

print(dijkstra([0,0],[N-1,N-1]))