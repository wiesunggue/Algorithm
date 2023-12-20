# https://www.acmicpc.net/problem/8980
# 백준 8980번 택배 문제

import sys
input = sys.stdin.readline

N,C = map(int,input().split())
M = int(input())
arr = [list(map(int,input().split())) for i in range(M)]
arr.sort(key=lambda x:(x[1],x[0]))
visit = [0] * (N+2)
total = 0
for start,end,cost in arr:
    m = max(visit[start:end])
    for t in range(start,end):
        visit[t] += min(cost,C-m)
    total += min(cost,C-m)

print(total)
