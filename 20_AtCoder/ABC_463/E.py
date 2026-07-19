import sys, heapq
input = sys.stdin.readline

N,M,Y = map(int,input().split())
Node = [[] for i in range(N+1)]
for i in range(M):
    v1,v2,T = map(int,input().split())
    Node[v1].append((T,v2))
    Node[v2].append((T,v1))

X = [0]+list(map(int,input().split()))

for i in range(N+1):
    Node[0].append((X[i],i))
    Node[i].append((X[i]+Y,0))

for i in range(N+1):
    Node[i].sort()

def dijkstra():
    pq = []
    cost = [10**10] * (N+1)
    cost[1] = 0
    heapq.heappush(pq,(0,1))
    while pq:
        print(pq)
        c, node = heapq.heappop(pq)

        if c > cost[node]:
            continue

        for n in range(len(Node[node])):
            new_c, new_node = Node[node][n]
            if cost[new_node] > c + new_c:
                cost[new_node] = c + new_c
                heapq.heappush(pq, (cost[new_node],new_node))
    print(*cost[2:],sep=' ')

# 1. 다익스트라 구현
# 2. 이 문제는 두 노드간 간선  + 워프 2가지 방식 이동을 정의함
# 3. 워프는 N * N 의 모든 노드가 연결되는 구조이나 모두 탐색하지 않도록 해야 함

dijkstra()