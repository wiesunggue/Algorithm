import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def ans():
    global posx, posy
    posx = [0,0,-1,1]
    posy = [-1,1,0,0]
    cnt1=0
    cnt2=0
    N = int(input().rstrip())
    visit=[[0 for _ in range(N)] for _ in range(N)]
    arr=[]
    for _ in range(N):
        arr.append(list(input().rstrip()))
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0:
                dfs(N,arr,visit,arr[i][j],i,j)
                cnt1+=1
    visit=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='G':
                arr[i][j]='R'
    for i in range(N):
        for j in range(N):
            if visit[i][j]==0:
                dfs(N,arr,visit,arr[i][j],i,j)
                cnt2+=1
    print(cnt1,cnt2)


def dfs(N,arr,visit,now,x,y):
    for i in range(4):
        a = x+posx[i]; b = y+posy[i]
        if (a>=0)&(a<N)&(b>=0)&(b<N):
            if (visit[a][b]==0)&(arr[a][b]==now):
                visit[a][b]=now
                dfs(N,arr,visit,now,a,b)


if __name__ == "__main__":
    ans()