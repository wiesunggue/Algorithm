# https://www.acmicpc.net/problem/14499
import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

command = list(map(int,input().split()))
direction = [(0,1),(0,-1),(-1,0),(1,0)]
dice = [0,0,0,0,0,0]
def rotate(dice, direction):
    if direction==1: # 동
        newdice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif direction==2: # 서
        newdice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif direction==3: # 북
        newdice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    elif direction==4: # 남
        newdice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    return newdice

for c in command:
    i,j = direction[c-1]
    x+=i
    y+=j
    #print(x,y)
    # 넘어갈 수 없는경우
    if x<0 or x>=N or y<0 or y>=M:
        x-=i
        y-=j
        continue
    dice = rotate(dice,c)
    if arr[x][y] == 0:
        arr[x][y] = dice[0]
    else:
        dice[0] = arr[x][y]
        arr[x][y] = 0
    print(dice[5])
