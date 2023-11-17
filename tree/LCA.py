# https://www.acmicpc.net/problem/11437
# 백준 11437번 LCA 문제

# 가장 가까운 공통 조상을 찾는 문제

import sys
sys.setrecursionlimit(10**5) # 재귀 허용횟수 증가
# 입력과 출력이 많으니 빠른 입출력이 필요하다.
input = sys.stdin.readline
print = sys.stdout.write

def find_parent(node,d):
    '''dfs로 각 노드으 부모 노드를 찾는 함수'''
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            parent[n] = node
            depth[n] = d
            find_parent(n,d+1)
def LCA(u,v):
    '''두 노드를 입력받아서 공통 조상을 찾는 함수'''
    if depth[u]>depth[v]:
        u,v = v,u
    while u != v:
        if depth[u] != depth[v]:
            v = parent[v]
        else:
            u,v = parent[u],parent[v]
    return u


# 트리 만들기
N = int(input())
tree = [[]for i in range(N+1)]
visit = [0] * (N+1)
parent = [0] * (N+1)
depth = [0] * (N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# 각 노드의 부모 찾기
visit[1] = 1
find_parent(1,1)

# 쿼리 처리하기
M = int(input())
for i in range(M):
    a,b = map(int,input().split())
    print(f'{LCA(a,b)}\n')
