# https://www.acmicpc.net/problem/20668
# 카트라이더 문제
import sys
from queue import PriorityQueue
from collections import deque
D = 3628800 # 10!값
input = sys.stdin.readline
N,M = map(int,input().split())

table=[[10**16 for i in range(11)]for j in range(N+1)]
visit=[[0 for i in range(11)]for j in range(N+1)]
Edge = [deque() for i in range(N+1)]

for i in range(M):
    a,b,c,d=map(int,input().split())
    Edge[a].append((b,c*D,d))
    Edge[b].append((a,c*D,d))

def dijkstra(start,end):
    pq = PriorityQueue()
    pq.put((0,1,start))
    table[start][1]=0
    while pq.empty()==False:
        score,speed,idx=pq.get()
        if table[idx][speed]<score:
            continue
        for i,l,k in Edge[idx]:
            for d in range(-1,2,1):
                nowspeed=d+speed
                if nowspeed<1 or nowspeed>k:
                    continue
                nowscore = score+l//nowspeed
                if table[i][nowspeed]>nowscore:
                    table[i][nowspeed]=nowscore
                    pq.put((nowscore,nowspeed,i))
    return table[end]


#print(dijkstra(1,N))
ans = min(dijkstra(1,N))
A=f'{ans//D}' # 정수부
B=f'{(ans%D)/D:.9f}' # 실수부
# 유효숫자 자리 때문에 정수와 실수부를 나눠서 계산해야 함...
print(A+B[1:])

