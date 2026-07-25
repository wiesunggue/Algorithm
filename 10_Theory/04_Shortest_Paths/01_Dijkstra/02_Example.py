# 1	13911	집 구하기	Gold II	멀티소스 다익스트라 2회
import heapq
from multiprocessing import heap
import sys

from ZOCA.A import B
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for i in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

M, x = map(int, input().split())
mac = list(map(int, input().split()))
S, y = map(int, input().split())
store = list(map(int, input().split()))

def dijkstra(start):
    pq = []

    visit = [False] * (V + 1)
    table = [float('inf')] * (V + 1)
    for s in start:
        heapq.heappush(pq, (0, s))
        table[s] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visit[node]:
            continue
        visit[node] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx]:
                table[idx] = cost + weight
                heapq.heappush(pq, (table[idx], idx))

    return table

t1 = dijkstra(mac)
t2 = dijkstra(store)
m = float('inf')
for i in range(1, V + 1):
    if t1[i]<=x and t2[i]<=y and i not in mac and i not in store:
        m = min(m, t1[i]+t2[i])

print(m if m != float('inf') else -1)


# 2	17835	면접보는 승범이네	Gold II	역방향 그래프 + 멀티소스
import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[v].append((u, w))

city = list(map(int, input().split()))

def dijkstra(start):
    pq = []

    visit = [False] * (N + 1)
    table = [float('inf')] * (N + 1)
    for s in start:
        heapq.heappush(pq, (0, s))
        table[s] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visit[node]:
            continue
        visit[node] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx]:
                table[idx] = cost + weight
                heapq.heappush(pq, (table[idx], idx))

    return table

t1 = dijkstra(city)
print(t1.index(max(t1)))
print(max(t1))
# 3	16681	등산	Gold II	이동 가능한 간선 제한 + 양방향 계산
import heapq
import sys
input = sys.stdin.readline
N, M, D, E = map(int, input().split())
height = [0] + list(map(int, input().split()))
graph = [[] for i in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def compare(a, b, greater = True):
    if greater:
        return a > b
    else:
        return a < b

def dijkstra(start, greater):
    pq = []

    visit = [False] * (N + 1)
    table = [float('inf')] * (N + 1)
    heapq.heappush(pq, (0, start))
    table[start] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        if visit[node]:
            continue
        visit[node] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx] and compare(height[idx], height[node], greater):
                table[idx] = cost + weight
                heapq.heappush(pq, (table[idx], idx))

    return table

t1 = dijkstra(1, True)
t2 = dijkstra(N, True)
m = float('-inf')
for i in range(2,N):
    if t1[i] != float('inf') and t2[i] != float('inf'):
        m = max(m, height[i]*E - (t1[i]+t2[i])*D)

print(m if m != float('-inf') else "Impossible")

# 4 1162	도로포장	Platinum V	dist[정점][포장 횟수] 상태 확장
N, M, K = map(int, input().split())
graph = [[] for i in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start, k):
    pq = []

    visit = [[False] * (k+1) for i in range(N+1)]
    table = [[float('inf')] * (k+1) for i in range(N+1)]
    heapq.heappush(pq, (0, start, 0))
    table[start][0] = 0

    while pq:
        cost, node, ith = heapq.heappop(pq)
        if visit[node][ith]:
            continue
        visit[node][ith] = True
        for idx, weight in graph[node]:
            if cost + weight < table[idx][ith]:
                table[idx][ith] = cost + weight
                heapq.heappush(pq, (table[idx][ith], idx, ith))
            if ith < k and cost < table[idx][ith+1]: # 해당 간선을 0으로 만드는 경우
                table[idx][ith+1] = cost
                heapq.heappush(pq, (table[idx][ith+1], idx, ith+1))

    return table

table = dijkstra(1,K)
print(min(table[N]))
# 5	16118	달빛 여우	Gold I	이동 속도 상태를 포함한 다익스트라
N, M = map(int ,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    pq = []
    fast_table = [float('inf')] * (N + 1)
    slow_table = [float('inf')] * (N + 1)
    fast_visit = [False] * (N + 1)
    slow_visit = [False] * (N + 1)

    fast_table[start] = 0
    heapq.heappush(pq, (fast_table[start], start, 0))

    while pq:
        cost, node, status = heapq.heappop(pq)
        if status == 1:
            if slow_visit[node] == True:
                continue
            slow_visit[node] = True
        elif status == 0:
            if fast_visit[node] == True:
                continue
            fast_visit[node] = True
            

        for n, c in graph[node]:
            if status == 0:
                if cost + c < slow_table[n]:
                    slow_table[n] = cost + c
                    heapq.heappush(pq, (slow_table[n], n, 1))

            if status == 1:
                if cost + 4*c < fast_table[n]:
                    fast_table[n] = cost + 4*c
                    heapq.heappush(pq, (fast_table[n], n, 0))
                

    table = [0] * (N+1)
    for i in range(N+1):
        table[i] = min(fast_table[i],slow_table[i])
    return table

wolf = dijkstra(1)
# fox는 일반 다익스트라 최단거리를 계산하면 되어 생략함.


# 6	13308	주유소	Platinum V	현재까지의 최저 기름값을 상태로 관리
import heapq
N, M = map(int, input().split())
arr = [0]+list(map(int, input().split()))
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    pq = []
    table = [[float('inf')] * 2501 for i in range(N+1)]
    visit = [False] * (N+1)

    heapq.heappush(pq, (0,start, arr[start]))
    table[start][arr[start]] = 0

    while pq:
        cost, node, price = heapq.heappop(pq)
        if table[node][price] == cost:
            continue
        for n, c in graph[node]:
            p = min(price, arr[n])
            if cost + c*price < table[n][p]:
                table[n][p] = cost + c*price
                heapq.heappush(pq, (table[n][p], n, p))

    return table

print(min(dijkstra(1)[N]))


# 7	14461	소가 길을 건너간 이유 7	Gold II	이동 횟수 mod 3 상태 확장
import heapq

N, T = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
x_move = [0,0,-1,1]
y_move = [-1,1,0,0]

def dijkstra(start):
    x,y = start
    pq = []
    table = [[[float('inf')] * 3 for _ in range(N)] for _ in range(N)]

    heapq.heappush(pq, (0, x, y, 0))
    table[x][y][0] = 0

    while pq:
        cost, x, y, cnt = heapq.heappop(pq)
        if table[x][y][cnt%3] != cost:
            continue

        for i in range(4):
            new_x = x+x_move[i]
            new_y = y+y_move[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if ((cnt+1)%3==0)*arr[new_x][new_y] + cost + T < table[new_x][new_y][(cnt+1)%3]:
                    table[new_x][new_y][(cnt+1)%3] = ((cnt+1)%3==0)*arr[new_x][new_y] + cost + T
                    heapq.heappush(pq, (table[new_x][new_y][(cnt+1)%3],new_x,new_y,cnt+1))

    return table

print(min(dijkstra((0,0))[N-1][N-1]))

# 8	24042	횡단보도	Gold I	현재 시각에 따른 대기시간 계산
import heapq
N, M = map(int, input().split())

# 9	28707	배열 정렬	Gold I	배열을 정점으로 보는 암시적 그래프
# 10	2307	도로검문	Gold I	최단경로 복원 + 간선 제거 후 재실행
# 11	5719	거의 최단 경로	Platinum V	모든 최단경로 간선 추적·제거

