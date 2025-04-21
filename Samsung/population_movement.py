# https://www.acmicpc.net/problem/16234
# 인구 이동
from collections import deque

visit_pos = [(0,1),(0,-1),(1,0),(-1,0)]
visit_cnt = 0
N,L,R = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
generation = 0
# dictioanary idx:{population, cnt}를 저장



def bfs(x,y):
    global visit_cnt,visit
    dq = deque()
    dq.append((x,y))
    visit[x][y] = visit_cnt
    population_dict[visit_cnt] = {'population':0,'count':0}
    while dq:
        x,y = dq.popleft()
        population_dict[visit_cnt]['population'] += arr[x][y]
        population_dict[visit_cnt]['count'] += 1

        for i in range(4):
            nx,ny = x+visit_pos[i][0],y+visit_pos[i][1]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==-1 and L<=abs(arr[x][y]-arr[nx][ny])<=R:
                visit[nx][ny] = visit_cnt
                dq.append((nx,ny))

    visit_cnt += 1

while True:
    visit = [[-1]*N for i in range(N)]
    population_dict = {}
    visit_cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1:
                bfs(i,j)
                print(i,j,generation,population_dict)
                print(*visit,sep='\n')
    # 인구 업데이트
    for i in range(N):
        for j in range(N):
            x = population_dict[visit[i][j]]
            p,c = x['population'],x['count']
            arr[i][j] = p//c

    if visit_cnt == N*N:
        break

    generation += 1

print(generation)