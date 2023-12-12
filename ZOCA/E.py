N,M=map(int,input().split())
arr=[input()for i in range(N)]
d={}
ans=True
i=0
j=0
while i<N or j<M:
    start=arr[i][j]
    tmp=0
    tmp2=0
    if (i-1)!=N:
        tmp=1
    while arr[i+tmp][j]==start:
        print('tmp',i,tmp,j)
        tmp+=1
        if (i+tmp)>=N-1:
            break

    if (j-1)!=M:
        tmp2=1
    while arr[i][j+tmp2]==start:
        tmp2+=1
        if (j+tmp2)>=M-1:
            break
    print(tmp,tmp2)
    for a in range(tmp):
        for b in range(tmp2):
            if start!=arr[i+a][j+b]:
                ans=False
    if ans==True:
        i+=tmp if tmp==1 else tmp-1
        j+=tmp2 if tmp2==1 else tmp2-1
    else:
        break
if ans==True:
    print('dd')
else:
    print('BaboBabo')