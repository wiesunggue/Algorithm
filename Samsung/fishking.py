# https://www.acmicpc.net/problem/17143
# 낚시왕

R,C,M = map(int,input().split())
arr = [[[-1 for j in range(C)] for i in range(R)],[[-1 for j in range(C)] for i in range(R)]]
direction = [(-1,0),(1,0),(0,1),(0,-1)]
convert_direction = {0:1,1:0,2:3,3:2}
fish_info = []
for i in range(M):
    r,c,s,d,z = map(int,input().split())
    if d == 1 or d == 2:
        s = s%(R*2-2)
    else:
        s = s%(C*2-2)
    fish_info.append((s,d-1,z))
    arr[0][r-1][c-1] = i
print(arr[0])
catched = 0
for fishing in range(C):
    # catch
    for i in range(R):
        if arr[fishing%2][i][fishing] != -1:
            catched += fish_info[arr[fishing%2][i][fishing]][2]
            arr[fishing%2][i][fishing] = -1
            break
    print('catch iteration')
    print(*arr[fishing%2],sep='\n')
    # fish move
    for i in range(R):
        for j in range(C):
            idx = arr[fishing % 2][i][j]
            if idx != -1:
                s,d,z = fish_info[idx]
                ns = s
                x,y = i,j
                while s != 0:
                    s -= 1
                    x,y = x+direction[d][0],y+direction[d][1]
                    if not (0<=x<R and 0<=y<C):
                        d = convert_direction[d]
                        x,y = x+2*direction[d][0],y+2*direction[d][1]

                fish_info[idx] = [ns,d,z]

                # 잡아먹기
                if arr[(fishing+1)%2][x][y] != -1:
                    before = arr[(fishing+1)%2][x][y]
                    if fish_info[idx][2] < fish_info[before][2]:
                        arr[(fishing+1)%2][x][y] = before
                    else:
                        arr[(fishing+1)%2][x][y] = idx
                else:
                    arr[(fishing+1)%2][x][y] = idx


    # 배열 초기화
    for i in range(R):
        for j in range(C):
            arr[fishing%2][i][j] = -1

    print('move iteration')
    print(*arr[(fishing+1)%2],sep='\n')
print(catched)