# https://www.acmicpc.net/problem/2961
# 도형이가 만든 맛있는 음식

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
subset = (1<<N)-1
print(bin(subset))
removed = subset
m=10**10
while subset:
    Sour = 1
    Bitter = 0
    for i in range(N):
        if subset&(1<<i):
            print(bin(subset),i)
            Sour*=arr[i][0]
            Bitter+=arr[i][1]
            
    print(Sour,Bitter)
    m=min(m,abs(Sour-Bitter))
    subset = (subset-1)&removed
    
print(m)