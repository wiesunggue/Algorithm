# https://www.acmicpc.net/problem/1595
# 백준 1595번 북쪽나라의 도로

import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# 트리의 크기가 처음에 주어지지 않음 -> 1만개의 도시가 있을 수 있음

# 1. 사이클이 없는 그래프 문제
# 2. 그래프의 최대 거리를 찾아야 한다
# 3. 임의의 노드로부터 최장 거리의 노드를 구한다.
# 4. 최장 거리의 노드에서 시작해서 최댓값을 구한다. -> 최장거리가 된다.
# 5. 최장 거리를 구하는 dfs 함수를 이용해서 임의의 점을 넣어서 한 노드를 찾고, 그것을 다시 넣어서 한 노드로 부터의 최장 거리를 구한다.

tree = [[] for i in range(10002)]
visit = [0] * (10002)
def dfs_find_node(node):
    '''임의의 노드로 부터 최장 거리의 노드를 구해 최장거리와 노드를 반환한다'''
    pq = []
    for n,w in tree[node]:
        if visit[n] != 1:
            visit[n] = 1
            dist,node = dfs_find_node(n)
            heapq.heappush(pq,(dist-w,node)) # 최소힙이므로 음수를 활용한다
    if pq:
        return heapq.heappop(pq)
    else:
        return 0,node

# 트리 입력받기 종료시점이 정해지지 않아서 EOF를 사용해야 한다
try:
    while True:
        a,b,c = map(int,input().split())
        tree[a].append((b,c))
        tree[b].append((a,c))
except:
    pass

max_node = []
ans_list = []
# 연결되지 않은 복수의 그래프가 존재하는 경우를 위해서 모든 노드 탐색을 진행함
for i in range(10001):
    if visit[i] != 1 and len(tree[i]) != 0:
        visit[i] = 1
        _,n1 = dfs_find_node(1)
        heapq.heappush(max_node,n1)
visit = [0] * (10001)

# 존재하는 K개의 그래프에 대해서 전부 탐색을 하고 그중 최댓값을 구한다
for n in max_node:
    heapq.heappush(ans_list,dfs_find_node(n1)[0])

print(heapq.heappop(ans_list))