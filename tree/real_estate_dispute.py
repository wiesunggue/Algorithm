# https://www.acmicpc.net/problem/20364
# 백준 20364번 부동산 다툼

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [int(input()) for i in range(M)]
pos = {}

for i in range(M):
    data = arr[i]
    ans = 0
    while data:
        if pos.get(data) != None:
            ans = data
        data //= 2
    if data == 0:
        pos[arr[i]] = 1
    print(ans)
