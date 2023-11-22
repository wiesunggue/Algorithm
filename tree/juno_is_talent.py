# https://www.acmicpc.net/problem/14657
# 백준 14657번 준오는 최종인재야 문제

import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
# 문재 해결 전략
# 1. 가장 많은 문제를 풀어야 함 => 연결된 노드의 수가 최대가 되도록 dfs탐색(트리의 지름과 같은 전략)
# 2. 가장 많은 문제를 푸는데 걸리는 최소의 시간을 계산해야 함 => 연결된 노드의 수가 최대가 될 때에 걸리는 시간
# 3. 연결된 노드의 수가 가장 길면서 최장거리가 되는 경우 =>
# 데이터를 입력받아 트리를 구성한다
N, T = map(int,input().split())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
for i in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def find_max_dist(node):
    '''DFS로 해당 노드에서 최장거리와 최장거리를 이루는 노드를 반환하는 함수'''
    node_num = 0
    node_dist = -10000000 if len(tree[node])!=1 or visit[node] == 2 else 0
    t = node
    for n,dist in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            result = find_max_dist(n)
            if (node_num, node_dist)<(result[0]+1,result[2]-dist):
                node_num = result[0]+1
                node_dist = result[2] - dist
                t = result[1]
    print(node,node_num,node_dist,t)
    return node_num,t,node_dist

# 임의의 노드에서 가장 많은 노드를 연결할 수 있는 노드를 찾는다
visit[1] = 2
num,node,dist = find_max_dist(1)
print("*********",num,node,dist)
# 1에서 최장거리인 node에서 탐색을 하여 찾은 node에서 가장 많은 노드를 연결할 수 있는 노드를 찾는다.
visit = [0] * (N+1)
visit[node] = 2
num,node,dist = find_max_dist(node)
print((-dist+T-1)//T) # T-1을 더해줘서 나누어서 나머지가 1이상인 경우에는 1을 추가하도록 한다(올림연산)
