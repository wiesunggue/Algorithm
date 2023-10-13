# https://www.acmicpc.net/problem/15661
# 링크와 스타트
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
def get_link_start(x):
    link= {}
    start={}
    for i in range(N):
        if (1<<i)&x:
            link[i]=1
        else:
            start[i]=1
    L,S=0,0
    for i in link.keys():
        for j in link.keys():
            L+=arr[i][j]
    for i in start.keys():
        for j in start.keys():
            S+=arr[i][j]
    return abs(L-S)
m=10**10
for i in range(2**N):
    m=min(m,get_link_start(i))
print(m)