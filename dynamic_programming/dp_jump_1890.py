#다이나믹 프로그래밍 점프 문제
#https://www.acmicpc.net/problem/1890
from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
arr=[list(map(int,input().split())) for i in range(N)]

def dp(x,y):
    visit = [[0 for i in range(N)] for i in range(N)]
    visit[x][y] = 1
    for i in range(N):
        for j in range(N):
            jump=arr[i][j]
            if jump==0:
                continue
            if jump+i<N:
                visit[i+jump][j]+=visit[i][j]
            if jump+j<N:
                visit[i][j+jump]+=visit[i][j]

            
    print(visit[-1][-1])
    
dp(0,0)