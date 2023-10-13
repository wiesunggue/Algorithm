#https://www.acmicpc.net/problem/10971
# 완전 탐색 외판워 순회2 문제
import sys
input = sys.stdin.readline
N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]
visit=[0]*N
m = 10 ** 9
def TSP(start,end,cost,count):
    global m
    if count==N and arr[start][end]!=0:
        m=min(m,cost+arr[start][end])
        return
        
    for i in range(N):
        if arr[start][i]!=0 and visit[i]==0:
            visit[i]=1
            TSP(i,end,cost+arr[start][i],count+1)
            visit[i]=0
visit[0]=1
TSP(0,0,0,1)
print(m)