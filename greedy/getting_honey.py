# https://www.acmicpc.net/problem/21758
# 꿀 따기 문제

N=int(input())
arr=list(map(int,input().split()))
psum=[0]*N
psum[0]=arr[0]
for i in range(1,N):
    psum[i]=psum[i-1]+arr[i]
print(psum)
honey=0
for i in range(N): # i는 벌통의 위치
    if i==0: # 벌집이 제일 왼쪽인 경우
        honey=max(honey,*(psum[N-2]-arr[k]+psum[k-1] for k in range(1,N)))
    elif i==N-1: # 벌집이 제일 오른쪽인 경우
        honey=max(honey,*(psum[N-1]-arr[0]+psum[N-1]-psum[k]-arr[k] for k in range(1,N)))
    else:
        for j in range(N): # 고려해야 하는 case 맨 왼쪽에 벌 vs 맨 오른쪽에 벌 하나
            if i==j:
                continue
            if i<j:
                if j!=N-1:
                    honey=max(honey,psum[N-2]-psum[i-1]+psum[j-1]-psum[i-1]-arr[j]) # 오른쪽에 있을 경우
                honey=max(honey,psum[i]-psum[0]+psum[j-1]-psum[i]) # 왼쪽에 있을 경우
            else:
                if j!=0:
                    honey=max(honey,psum[i]-psum[0]+psum[i]-psum[j+1]-arr[j])# 왼쪽에 있을 경우
                honey=max(honey,psum[N-2]-psum[i-1]+psum[i]-psum[j+1]) #오른쪽에 있을 경우\
print(honey)