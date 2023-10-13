import sys
global cnt
sys.setrecursionlimit(10**5)
rinput = sys.stdin.readline
pos = {"U":(-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}
N,M = map(int,input().split())
arr = [list(input()) for i in range(N)]
chk = [[[j,i]for i in range(M)] for j in range(N)]
visit = [[0for i in range(M)] for j in range(N)]
print(*arr,sep='\n')

def dfs(x,y):
    global cnt
    if visit[x][y]==0:
        visit[x][y]=cnt
        new_x,new_y = pos[arr[x][y]]
        new_x+=x
        new_y+=y
        dfs(new_x,new_y)
        visit[x][y]=cnt
    else:
        cnt = visit[x][y]
    return
cnt=1
tmp=1
for i in range(N):
    for j in range(M):
        if visit[i][j]==0:
            cnt=tmp
            dfs(i,j)
            if cnt==tmp:
                tmp += 1
                
                
print(tmp-1)