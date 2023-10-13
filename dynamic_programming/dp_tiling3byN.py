#https://www.acmicpc.net/problem/2133
# 타일 채우기
# 3*N의 타일을 채우기

N=int(input())
cache=[-1]*1000
cache[0],cache[2]=0,3
def tiling(N):
    if N==0:
        return 1
    if N<0:
        return 0
    if N%2==1:
        return 0
    if cache[N]!=-1:
        return cache[N]
    ret=tiling(N-2)*3
    for i in range(2,N):
        ret+=tiling(N-2*i)*2
    cache[N]=ret
    return ret
print(tiling(N))

