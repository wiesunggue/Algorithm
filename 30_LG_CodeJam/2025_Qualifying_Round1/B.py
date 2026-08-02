import sys
import heapq
input = sys.stdin.readline
INF = 10**30
N, K = map(int, input().split())
arr = []
for i in range(N):
    S,E,P,D = map(int, input().split())
    arr.append((S,E,P,D))

arr.sort()
idx = 0
pq = []
cost = 0
diff = 0
ans = float('inf')
d = arr[0][0]

while idx < N or pq:
    while pq and pq[0][0] < d:
        _, i = heapq.heappop(pq)

        S, E, P, D = arr[i]

        cost -= P - D * ((d - 1) - S)
        diff -= D

    cost -= diff

    while idx < N and arr[idx][0] == d:
        S, E, P, D = arr[idx]

        heapq.heappush(pq, (E, idx))

        cost += P
        diff += D
        idx += 1

    if len(pq) >= K:
        ans = min(ans, cost)

    # 다음으로 활성 아이템 집합이 변하는 날짜
    next_start = arr[idx][0] if idx < N else INF
    next_end = pq[0][0] + 1 if pq else INF

    next_d = min(next_start, next_end)

    if next_d == INF:
        break

    gap = next_d - d - 1

    if gap > 0:
        cost -= diff * gap

        if len(pq) >= K:
            ans = min(ans, cost)

    d = next_d
print(ans if ans != float('inf') else -1)