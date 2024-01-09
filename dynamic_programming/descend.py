import heapq,sys
sys.setrecursionlimit(10**5)
pq = []
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
dp = [[0]*M for i in range(N)]
dp[0][0]=1
ans = [[0]*M for i in range(N)]
xpos = [-1,1,0,0]
ypos = [0,0,-1,1]
def find():
    pq = []
    heapq.heappush(pq,(-arr[0][0],0,0))
    visit = [[[0]*4 for j in range(M)] for i in range(N)]
    visit[0][0]=0
    while pq:
        height,x,y = heapq.heappop(pq)
        print(x,y)
        for i in range(4):
            new_x,new_y = x+xpos[i],y+ypos[i]
            if 0<=new_x<N and 0<=new_y<M and arr[new_x][new_y]<-height and visit[new_x][new_y][i]==0:
                visit[new_x][new_y][i]=1
                heapq.heappush(pq,(-arr[new_x][new_y],new_x,new_y))
                dp[new_x][new_y] += dp[x][y]

find()
print(*dp,sep='\n')
print(dp[N-1][M-1])