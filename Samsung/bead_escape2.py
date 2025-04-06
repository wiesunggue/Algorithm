import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(input()) for i in range(N)]
idx = 0
direction = [(-1,0),(1,0),(0,1),(0,-1)]

def moveTo(bead,wall,d,state):
    x,y = direction[d]
    i,j = bead
    while arr[i][j] != '#' and arr[i][j] != 'O' and ((i,j) != wall or state):
        i += x
        j += y
    goal = arr[i][j] == 'O'
    return (i-x,j-y),goal
def bfs():
    ans = -1
    stop = False
    redgoal,bluegoal = False,False
    for i in range(N):
        for j in range(M):
            if arr[i][j] =='B':
                blue = i,j
            if arr[i][j] == 'R':
                red = i,j

    dq = deque()
    dq.append((0,blue,red,0))
    dq.append((1,blue,red,0))
    dq.append((2,blue,red,0))
    dq.append((3,blue,red,0))
    while dq and stop==False:
        direction,blue,red,cnt = dq.popleft()
        for i in range(4):
            if cnt == 10:
                continue
            newred, redgoal = moveTo(red,blue,i,False)
            newblue,bluegoal = moveTo(blue,newred,i,redgoal)
            newred, redgoal = moveTo(newred,newblue,i,bluegoal)
            if redgoal == True and bluegoal == False:
                ans = cnt + 1
                stop = True
                break
            if redgoal != True and bluegoal != True:
                dq.append((i,newblue,newred,cnt+1))

    return ans

print(bfs())