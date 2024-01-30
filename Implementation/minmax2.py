# https://www.acmicpc.net/problem/20053
# 백준 20053번 최소, 최대 2 문제

import sys
input = sys.stdin.readline
def minmax(arr):
    M = m = int(arr[0])

    for i in arr:
        t=int(i)
        M = max(M,t)
        m = min(m,t)
    return m,M
T = int(input())
for t in range(T):
    N = int(input())
    print(T,N)
    print(*minmax(input().split()))