# https://www.acmicpc.net/problem/12896
# 백준 12896번 스크루지 민호

# 임의의 노드에서 출발하여 트리의 최장거리를 구하고, 해당 노드에서 최장거리를 다시 탐색하면 해당 그래프 내에서 가장 긴 거리를 구할 수 있다.
# dfs의 반환값은 dist, node로 정의
# 가장 긴 거리 = dfs(dfs(start)[1])[0]
# 간선간 가중치는 1이므로 (가장 긴 거리+1)//2 = 정답
import sys
sys.setrecursionlimit(10**5+1)
input = sys.stdin.readline

N = int(input())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def find_max_dist(node):
    '''DFS로 해당 노드에서 최장거리와 최장거리를 이루는 노드를 반환하는 함수'''
    dist = 0
    t = node
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            result = find_max_dist(n)
            if dist<result[0]+1:
                dist = result[0]+1
                t = result[1]
    return dist,t

start = 1
visit[start] = 1
start = find_max_dist(start) # 노드 1번에서 가장 먼 노드와 거리
visit = [0] * (N+1)
end = find_max_dist(start[1]) # start 지점에서 가장 멀리 있는 노드 end와 거리
print((end[0]+1)//2)