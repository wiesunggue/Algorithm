# https://www.acmicpc.net/problem/16194
# 카드 구매하기2

T=int(input())
for test in range(T):
    N=int(input())
    arr=[0]+list(map(int,input().split()))
    M=int(input())
    cache=[0]*(M+1)
    cache[0]=1
    for i in range(1,N+1):
        for j in range(arr[i],M+1):
            cache[j]+=cache[j-arr[i]]
    print(cache[M])
    