# https://www.acmicpc.net/problem/16236
# 아기 상어 문제
from collections import deque

N = int(input())
fish = [list(map(int,input().split())) for i in range(N)]
xpos = [0,0,-1,1]
ypos = [-1,1,0,0]
timer = 0
stopIteration = False
class Shark:
    def __init__(self,x,y):
        self.size = 2
        self.x = x
        self.y = y
        self.count = 0

    def sizeup(self):
        self.size += 1

    def eat(self):
        self.count += 1
        if self.count == self.size:
            self.size += 1
            self.count = 0

    def move(self,x,y):
        self.x = x
        self.y = y
        self.eat()

    def getPos(self):
        return self.x,self.y
    def getsize(self):
        return self.size

for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            shark = Shark(i,j)
            fish[i][j] = 0

def findFeed():
    global shark, timer, stopIteration
    x,y = shark.getPos()
    dq = deque()
    dq.append((x,y,0))
    visit = [[-1]*N for i in range(N)]
    visit[x][y] = 0
    iterconstraint = 10**10
    feed = [-1,-1]
    feed = []
    while dq:
        print(dq)
        x,y,t = dq.popleft()

        for i in range(len(xpos)):
            nx,ny = x+xpos[i],y+ypos[i]
            if 0<=nx<N and 0<=ny<N and fish[nx][ny] <= shark.getsize() and visit[nx][ny] == -1:
                if iterconstraint == visit[x][y]:
                    continue
                visit[nx][ny] = visit[x][y] + 1
                dq.append((nx,ny,visit[nx][ny]))

                if fish[nx][ny] != 0 and fish[nx][ny] < shark.getsize():
                    iterconstraint = visit[nx][ny]
                    feed.append((nx,ny))

    print(*visit,sep='\n')
    if iterconstraint == 10**10:
        stopIteration = True
    else:
        feed.sort(key = lambda a: (a[0], a[1]))
        x,y = feed[0]
        shark.move(x,y)
        fish[x][y] = 0
        timer += iterconstraint

while stopIteration == False:
    print('size',shark.getsize())
    print(*fish,sep='\n')
    findFeed()

print(*fish,sep='\n')
print(timer)