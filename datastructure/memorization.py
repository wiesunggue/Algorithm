# https://www.acmicpc.net/problem/2776
# 백준 2776번 암기왕
from collections import defaultdict
import sys
input = sys.stdin.readline
print = sys.stdout.write
def solution():
    N = int(input())
    arr = list(map(int,input().split()))
    d = defaultdict(int)
    for i in range(N):
        d[arr[i]] = 1
    M = int(input())
    brr = list(map(int,input().split()))
    for i in range(M):
        print(f'{d[brr[i]]}\n')
T = int(input())
for test in range(T):
    solution()
