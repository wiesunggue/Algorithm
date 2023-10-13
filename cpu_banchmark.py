# https://www.acmicpc.net/problem/20312
# CPU 밴치마킹

import sys
input = sys.stdin.readline
MAX_NUM = 10**9+7
N = int(input())-1
arr = list(map(int,input().split()))
before=arr[0]
cnt=before
for i in range(1,N):
    after=(before+1)*arr[i]
    before=after%MAX_NUM
    cnt+=after
    cnt=cnt%MAX_NUM
print(cnt)