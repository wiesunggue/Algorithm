# https://www.acmicpc.net/problem/19598
# 백준 19598번 최소 회의실 개수 문제
import heapq,sys
N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
arr.sort()
pq = [2**32]
cnt = 0
for i in range(N):
    while arr[i][0]>=pq[0]:heapq.heappop(pq)
    heapq.heappush(pq,arr[i][1])
    cnt = max(cnt,len(pq))
print(cnt-1)