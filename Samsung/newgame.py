# https://www.acmicpc.net/problem/17837
# 새로운 게임2

N,K = map(int,input().split())
direction = [(0,1),(0,-1),(-1,0),(1,0)]
convert_direction = {0:1,1:0,2:3,3:2}
generation = 0
stopGeneration = False
chess = []

arr = [list(map(int,input().split())) for i in range(N)]
chessList = [[[] for i in range(N)] for j in range(N)]

for idx in range(K):
    a,b,d = map(int,input().split())
    chess.append((a-1,b-1,d-1))
    chessList[a-1][b-1].append(idx)

while not stopGeneration:
    generation += 1
    for i in range(K):
        x,y,d = chess[i]
        nx,ny = x+direction[d][0],y+direction[d][1]
        idx = 0
        print(generation,i,"!!!!",chess[i])
        for pos in range(len(chessList[x][y])):
            if chessList[x][y][pos] == i:
                idx = pos
                break
        print(i,pos,idx,chessList[x][y])
        # 파란색
        if 0>nx or nx>=N or 0>ny or ny>=N or arr[nx][ny] == 2:
            d = convert_direction[d]
            nx, ny = x + direction[d][0], y + direction[d][1]
            chess[i] = (x, y, d)
            if 0>nx or nx>=N or 0>ny or ny>=N or arr[nx][ny] == 2:
                pass
            elif arr[nx][ny] == 0:
                chessList[nx][ny].extend(chessList[x][y][idx:])
                if len(chessList[nx][ny])>=4:
                    stopGeneration = True
                for pos in chessList[x][y][idx:]:
                    chess[pos] = (nx, ny, chess[pos][2])
                chessList[x][y] = chessList[x][y][:idx]
            elif arr[nx][ny] == 1:
                chessList[nx][ny].extend(reversed(chessList[x][y][idx:]))
                if len(chessList[nx][ny])>=4:
                    stopGeneration = True
                for pos in chessList[x][y][idx:]:
                    chess[pos] = (nx, ny, chess[pos][2])
                chessList[x][y] = chessList[x][y][:idx]

        # 흰색
        elif arr[nx][ny] == 0:
            chessList[nx][ny].extend(chessList[x][y][idx:])
            if len(chessList[nx][ny])>=4:
                stopGeneration = True
            for pos in chessList[x][y][idx:]:
                chess[pos] = (nx,ny,chess[pos][2])
            chessList[x][y] = chessList[x][y][:idx]
        # 빨간색
        elif arr[nx][ny] == 1:
            chessList[nx][ny].extend(reversed(chessList[x][y][idx:]))
            if len(chessList[nx][ny])>=4:
                stopGeneration = True
            for pos in chessList[x][y][idx:]:
                chess[pos] = (nx,ny,chess[pos][2])
            chessList[x][y] = chessList[x][y][:idx]

        print(*chessList, sep='\n')


    if generation >= 1000:
        stopGeneration = True

if generation>= 1000:
    print(-1)
else:
    print(generation)