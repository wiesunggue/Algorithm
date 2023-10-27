# https://www.acmicpc.net/problem/2346
# 백준 2346번 풍선 터트리기

from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
ans = deque()
N = int(input())
# N개의 풍선 추가하기
for i in range(N):
    dq.append(i+1)

arr = list(map(int,input().split()))
for i in range(N-1):
    print(dq)
    ans.append(dq.popleft())
    t = arr[ans[-1]-1] # 이동 위치 결정하기
    if t>0:
        for i in range(t-1):
            dq.append(dq.popleft())
    else:
        for i in range(-t):
            dq.appendleft(dq.pop())
ans.append(dq.pop())
print(*ans)