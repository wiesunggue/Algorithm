# https://www.acmicpc.net/problem/22864
# 백준 22864번 피로도 문제

A,B,C,M = map(int,input().split())
fat,work = 0,0
for i in range(24):
    if fat+A>M:
        fat -= C
        fat = max(0,fat)
        continue
    fat += A
    work += B

print(work)