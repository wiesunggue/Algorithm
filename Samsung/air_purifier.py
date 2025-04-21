# https://www.acmicpc.net/problem/17144
# 공기 청정기

R,C,T = map(int,input().split())
xpos = [0,0,-1,1]
ypos = [-1,1,0,0]
clockwisedirection = [(-1,0),(0,1),(1,0),(0,-1)]
counterclockwisedirection = [(1,0),(0,1),(-1,0),(0,-1)]
dust = [[list(map(int,input().split())) for i in range(R)],[[0 for i in range(C)] for j in range(R)]]


for i in range(R):
    if dust[0][i][0] == -1:
        downfaility = (i,0)
        upfaility = (i-1,0)


print(upfaility,downfaility)
dust[0][downfaility[0]][0] = 0
dust[0][upfaility[0]][0] = 0

for gen in range(T):

    # 초기화
    for i in range(R):
        for j in range(C):
            dust[(gen+1)%2][i][j] = dust[gen%2][i][j]
    print('확산 전 먼지')
    print(*dust[(gen+1)%2],sep='\n')

    # 확산
    for i in range(R):
        for j in range(C):
            diffusion = dust[gen%2][i][j]//5
            if (i,j) == upfaility or (i,j) == downfaility or diffusion==0:
                continue
            for idx in range(4):
                a = i + xpos[idx]
                b = j + ypos[idx]
                if (a,b) == upfaility or (a,b) == downfaility:
                    continue
                if 0<=a<R and 0<=b<C:
                    dust[(gen+1)%2][a][b] += diffusion
                    dust[(gen+1)%2][i][j] -= diffusion
    print('확산 후 먼지')
    print(*dust[(gen+1)%2],sep='\n')
    # 정화
    x,y = upfaility
    directioncount = 0
    nx,ny = -1,-1
    while directioncount!=4:
        dx, dy = clockwisedirection[directioncount]
        nx,ny = x+dx,y+dy
        if 0<=nx<=upfaility[0] and 0<=ny<C:
            dust[(gen+1)%2][x][y] = dust[(gen+1)%2][nx][ny]
            x,y = nx,ny
        else:
            directioncount += 1

    x,y = downfaility
    directioncount = 0
    nx,ny = -1,-1
    while directioncount!=4:
        dx, dy = counterclockwisedirection[directioncount]
        nx,ny = x+dx,y+dy
        if downfaility[0]<=nx<R and 0<=ny<C:
            dust[(gen+1)%2][x][y] = dust[(gen+1)%2][nx][ny]
            x,y = nx,ny
        else:
            directioncount += 1

    dust[(gen + 1) % 2][upfaility[0]][y] = 0
    dust[(gen + 1) % 2][downfaility[0]][y] = 0
    dust[(gen + 1) % 2][upfaility[0]][y+1] = 0
    dust[(gen + 1) % 2][downfaility[0]][y+1] = 0

    print('정화 후 먼지')
    print(*dust[(gen+1)%2],sep='\n')

print(sum(map(sum,dust[T%2])))