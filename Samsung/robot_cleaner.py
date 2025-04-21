# https://www.acmicpc.net/problem/14503
# 로봇 청소기
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
x,y,d = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

direction = [(-1,0),(0,1),(1,0),(0,-1)]
cnt = 0
while 1:
    # 더 이상 움직이지 못하는 경우
    if x < 0 or x >= N or y < 0 or y >= M or arr[x][y] == 1:
        break

    # 1. 청소되지 않은 경우 청소
    if arr[x][y] == 0:
        arr[x][y] = -1
        cnt += 1
    print(x,y)
    print(*arr,sep='\n')

    clean = True
    # 2. 4칸 모두 청소가 되어있는 경우
    for i in range(4):
        new_x,new_y = x+direction[i][0],y+direction[i][1]
        if 0 <= new_x < N and 0 <= new_y < M and arr[new_x][new_y] == 0:
            clean = False

    if clean:
        x,y = x-direction[d][0],y-direction[d][1]
        continue

    # 3. 4칸 중 하나가 청소가 안 되어있는 경우
    clean = False
    d -= 1
    d %= 4
    new_x,new_y = x+direction[d][0], y+direction[d][1]
    if 0 <= new_x < N and 0 <= new_y < M and arr[new_x][new_y] == 0:
        x,y = new_x,new_y



print(x,y,cnt)