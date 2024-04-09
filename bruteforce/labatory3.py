# https://www.acmicpc.net/problem/17142
# 백준 17142번 연구소3 문제
import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int,input().split())
virus = [list(map(int,input().split())) for i in range(N)]
posx = [0,0,-1,1]
posy = [-1,1,0,0]

# 비활성 바이러스의 위치와 개수 세기
virus_list = []
for i in range(N):
    for j in range(N):
        if virus[i][j]==2:
            virus_list.append((i,j))
number_virus = len(virus_list)

# 3차원 dp구성
visit = [[[10**4 if virus[j][i]!=1 else 0 for i in range(N)] for j in range(N)] for k in range(number_virus+1)]
visit_now = [[[10 ** 4 for i in range(N)] for j in range(N)] for k in range(number_virus+1)]

used_virus = [0]*number_virus
minimum_ans = 10**10
def find_time():
    m = 0
    for i in range(N):
        for j in range(N):
            if virus[i][j]==0:
                m = max(m,visit[M][i][j])
    return m

def backtracking(i):
    global minimum_ans
    if sum(used_virus)==M:
        minimum_ans  = min(minimum_ans,find_time())

    for j in range(i+1,number_virus):
        used_virus[j]=1
        merge_result(sum(used_virus),j)
        backtracking(j)
        used_virus[j]=0

def bfs(j):
    qu = deque()
    x,y = virus_list[j]
    visit_now[j][x][y] = 0
    qu.append((x,y))
    while qu:
        x,y = qu.popleft()
        for i in range(4):
            new_x,new_y = x+posx[i],y+posy[i]
            if 0<=new_x<N and 0<=new_y<N and visit_now[j][new_x][new_y]==10**4 and virus[new_x][new_y] != 1:
                visit_now[j][new_x][new_y] = visit_now[j][x][y]+1
                qu.append((new_x,new_y))

def merge_result(n,pos):
    for i in range(N):
        for j in range(N):
            visit[n][i][j] = min(visit[n-1][i][j],visit_now[pos][i][j])

for i in range(number_virus):
    bfs(i)

backtracking(-1)
if minimum_ans<10**4:
    print(minimum_ans)
else:
    print(-1)

