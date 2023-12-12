def generation(n,k):
    for i in range(100):
        if k<n+i*(i+1)//2:
            break
    # 여기서 i가 가능한 k의 최선이다.
    i=i-1
    arr=[0]*n
    tmp=2
    for j in range(n):
        if j<n-i:
            arr[j]=j+1
        else:
            arr[j]=arr[j-1]+tmp
            tmp+=1
    print(*arr)
    
T=int(input())
for test in range(T):
    n,k=map(int,input().split())
    generation(n,k)
    