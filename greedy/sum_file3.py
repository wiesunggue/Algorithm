# https://www.acmicpc.net/problem/13975
# 백준 13975번 파일 합치기 3 문제

import heapq,sys
input = sys.stdin.readline
def solutions():
    N = int(input())
    arr = list(map(int,input().split()))
    pq = []
    ans = 0
    for i in range(N):
        heapq.heappush(pq,arr[i])
    while len(pq)!=1:
        ans1 = heapq.heappop(pq)
        ans2 = heapq.heappop(pq)
        ans += ans1+ans2
        heapq.heappush(pq,ans1+ans2)
    print(ans)


T = int(input())
for test in range(T):
    solutions()