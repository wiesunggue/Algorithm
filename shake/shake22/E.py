import sys
input = sys.stdin.readline
print = sys.stdout.write
N,Q = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]
psum = [[arr[j][0] if i==0 else 0 for i in range(N)]for j in range(N)]
print(*psum,sep='\n')
for i in range(N):
    for j in range(1,N):
        psum[i][j]=arr[i][j]+psum[i][j-1]
print(*psum,sep='\n')

def query(x,y,jump):
    m=10**9
    for i in range(y,N):
        print(i)
        for j in range(x-jump+1):
            print('jjjjjj',j)
            m = min(m,psum[x][i-1]-psum[x][y-1]+psum[j][N-1]-psum[j][i-1])
#            print(m,x,y,i,j,psum[x][i-1]-psum[x][y-1],psum[j][N-1]-psum[j][i-1])
    return m

for i in range(Q):
    x,y,jump=map(int,input().split())
    x,y=x-1,y-1
    print(f'{query(x,y,jump)}\n')
    print('*****')