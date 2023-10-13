# https://www.acmicpc.net/problem/9084
import sys
input=sys.stdin.readline
test=int(input())

def solve(arr,target):
    cache = [[0]for _ in range(target+1) for _ in range(len(arr))]
    for money in arr:
        cache[money]=1
    count=0
    arr=reversed(arr)

for t in range(test):
    coin=int(input())
    arr=list(map(int,input().split()))
    target=int(input())
    solve(arr,target)