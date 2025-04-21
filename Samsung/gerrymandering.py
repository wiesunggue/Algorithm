# https://www.acmicpc.net/problem/17779
# 게리맨더링 2

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
mark = [[0]*N for i in range(N)]
def find_diff(x,y,d1,d2):
    if not (d1>=1 and d2>=1 and 0<=x<x+d1+d2<N and 0<=y-d1<y<y+d2<N):
        return 10**10

    area = [0,0,0,0,0]
    for i in range(N):
        for j in range(N):
            if i<x+d1 and j<=y and i < x+y-j:
                area[0] += arr[i][j]
                mark[i][j] = 1
            elif i<=x+d2 and j>y and i < x+j-y:
                area[1] += arr[i][j]
                mark[i][j] = 2
            elif i>=x+d1 and j<y-d1+d2 and i>x+d1+j+d1-y:
                area[2] += arr[i][j]
                mark[i][j] = 3
            elif i>x+d2 and j>=y-d1+d2 and i>x+d2+y+d2-j:
                area[3] += arr[i][j]
                mark[i][j] = 4
            else:
                area[4] += arr[i][j]
                mark[i][j] = 5
    if max(area) - min(area) == 23:
        print(*mark, sep='\n')
        print(area)
    return max(area)-min(area)

ans = 10**10
for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                ans = min(ans,find_diff(x,y,d1,d2))

print(ans)
find_diff(2,4,3,1)
print(*mark,sep='\n')