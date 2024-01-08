# https://www.acmicpc.net/problem/2228
# 백준 2228번 구간 나누기 문제

N,M = map(int,input().split())
arr = [int(input()) for i in range(N)]
psum = [0]+[arr[0]]*N
for i in range(1,N):
    psum[i+1] = psum[i] +arr[i]

cache = [[-10**10 for j in range(N+1)] for i in range(M+1)]
cache[0] = [0] * (N+1)

def select2():
    for usedRange in range(M):
        for pos in range(-1 if usedRange==0 else 0,N):
            for i in range(pos+1,N):
                for j in range(i,N):
                    if usedRange<M:
                        cache[usedRange+1][j] = max(cache[usedRange+1][j],cache[usedRange+1][j-1],cache[usedRange][pos-1]+psum[j+1]-psum[i])


select2()
print(*cache,sep='\n')
print(cache[M][N-1])