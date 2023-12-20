# https://www.acmicpc.net/problem/15724
# 백준 15724번 주지수 문제
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]

psum =[[0]*(M+1) for i in range(N+1)]
for i in range(N):
    psum[i][0] = arr[i][0] + psum[i-1][0]
    for j in range(1,M):
        psum[i][j] = psum[i][j-1] + psum[i-1][j] + arr[i][j] - psum[i-1][j-1]

def query(x1,y1,x2,y2):
    return str(psum[x2-1][y2-1]+psum[x1-2][y1-2]-psum[x2-1][y1-2]-psum[x1-2][y2-1])

K = int(input())
answer = [query(*list(map(int,input().split()))) for i in range(K)]

print('\n'.join(answer))