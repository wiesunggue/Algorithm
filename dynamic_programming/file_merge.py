# https://www.acmicpc.net/problem/11066
# 백준 11066번 파일 합치기 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def find(i,j):
    global cache
    if j-i == 0:
        return cache[i][j]
    if j-i == 1:
        return arr[i]+arr[j]
    if cache[i][j] != 0:
        return cache[i][j]
    z = 10**10
    for k in range(i,j):
        z = min(z,find(i,k)+find(k+1,j)+psum[j]-psum[i-1])
    cache[i][j] = z
    return cache[i][j]

T = int(input())
for test in range(T):
    N = int(input())
    arr = [0]+list(map(int,input().split()))
    psum = [0]*(N+1)
    for i in range(1,N+1):
        psum[i] = psum[i-1]+arr[i]
    print(psum)
    # 식 정의 i번부터 j-1까지 최소의 합 = cache[i][j]
    cache = [[0]*(N+1) for i in range(N+1)]
    find(1,N)
    print(cache[1][N])
