# https://www.acmicpc.net/problem/15683
# 감시 문제

import sys
input = sys.stdin.readline
N, M = map(int,input().split())

arr = [list(map(int,input().split())) for i in range(N)]
visit = [[0]*M for i in range(N)]
camera = []
direction = [(0, 1), (-1, 0),(0, -1), (1, 0)]
ans = 2**20
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            camera.append((i,j))

def writeDirection(x,y,d,cnt):
    while True:
        x,y = x+direction[d][0],y+direction[d][1]
        if 0<=x<N and 0<=y<M and arr[x][y] != 6:
            visit[x][y] ^= 1<<cnt
        else:
            break
def countZero():
    cnt = 0
    for i in range(N):
        for j in range(M):
            cnt += (visit[i][j]==0) and arr[i][j]==0
    return cnt
def backtracking(idx):
    global ans
    if idx == len(camera):
        print(*visit,sep='\n')
        ans = min(ans,countZero())
        return
    x,y = camera[idx]
    type = arr[x][y]

    if type == 5:
        for d in range(4):
            writeDirection(x,y,d,idx)
        backtracking(idx+1)
        for d in range(4):
            writeDirection(x,y,d,idx)

    elif type == 2:
        for i in range(2):
            writeDirection(x,y,i,idx)
            writeDirection(x,y,i+2,idx)
            backtracking(idx+1)
            writeDirection(x,y,i,idx)
            writeDirection(x,y,i+2,idx)
    elif type==1:
        for i in range(4):
            writeDirection(x,y,i,idx)
            backtracking(idx+1)
            writeDirection(x,y,i,idx)
    elif type==3:
        for i in range(4):
            writeDirection(x,y,i,idx)
            writeDirection(x,y,(i+1)%4,idx)
            backtracking(idx+1)
            writeDirection(x,y,i,idx)
            writeDirection(x,y,(i+1)%4,idx)
    elif type==4:
        for i in range(4):

            writeDirection(x,y,i,idx)
            writeDirection(x,y,(i+1)%4,idx)
            writeDirection(x,y,(i+2)%4,idx)
            backtracking(idx+1)
            writeDirection(x,y,i,idx)
            writeDirection(x,y,(i+1)%4,idx)
            writeDirection(x,y,(i+2)%4,idx)
backtracking(0)
print(ans)