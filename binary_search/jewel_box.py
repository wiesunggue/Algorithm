# https://www.acmicpc.net/problem/2792
# 백준 2792번 보석 상자 문제

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [int(input()) for i in range(M)]

def findmax(max_value):
    student = N
    for i in arr:
        student -= (i+max_value-1)//max_value

    return student>=0

start,end = 0,10**10
for i in range(100):
    mid = (start+end)//2
    if findmax(mid)==True:
        end = mid
    else:
        start = mid + 1

print(start,end)