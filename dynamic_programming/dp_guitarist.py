#https://www.acmicpc.net/problem/1495
# 기타리스트 문제

N,S,M=map(int,input().split())
volumn_diff=list(map(int,input().split()))
cache=[[-1 for i in range(M+10)]for j in range(N+10)]
cache[0][S]=1
ans=-1

def dp():
    for i in range(N):
        for j in range(M+10):
            if cache[i][j]!=-1:
                v=volumn_diff[i]
                if j+v<=M:
                    cache[i+1][j+v]=1
                if j-v>=0:
                    cache[i+1][j-v]=1
                
dp()
ans=(i if cache[N][i]!=-1 else -1for i in range(M+10))
print(max(ans))