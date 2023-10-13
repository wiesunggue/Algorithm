xpos=[0,0,-1,1]
ypos=[-1,1,0,0]
N,M = map(int,input().split())
arr=[input().replace('.','D') for i in range(N)]
chk=1
for i in range(N):
    for j in range(M):
        if arr[i][j]=='W':
            for k in range(4):
                x,y=i+xpos[k],j+ypos[k]
                if x>=0 and y>=0 and x<N and y<M and arr[x][y]=='S':
                    chk=0

print(chk)
if chk==1:
    print(*arr,sep='\n')