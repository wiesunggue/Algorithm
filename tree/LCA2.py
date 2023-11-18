# https://www.acmicpc.net/problem/11438
# 백준 11438번 LCA2 문제

# 희소 행렬을 활용해서 기존의 LCA를 더 최적화 하여 빠른 속도로 문제를 해결하는 문제
import sys
from collections import deque
# 빠른 입출력과 재귀 기본 처리
sys.setrecursionlimit(10**5+1)
input = sys.stdin.readline
print = sys.stdout.write

def find_parent(node,d):
    '''dfs로 각 노드의 depth와 Parent를 반환한다'''
    dq = []
    dq.append((0,1))
    while dq:
        pnode,node = dq.pop()
        depth[node] = depth[pnode]+1
        for n in tree[node]:
            if n != pnode:
                parent[n] = node
                dq.append((node,n))

def make_sparse_table():
    '''희소 행렬을 구성한다.'''
    # 1번 노드의 부모는 0번을 가르키도록 한다
    for i in range(20):
        for j in range(N+1):
            if i==0:
                sparse_table[j][i] = j # 희소 행렬[x][0]은 자기자신
            elif i==1:
                sparse_table[j][i] = parent[j] # 희소 행렬[x][1]은 부모 노드
            else:
                sparse_table[j][i] = sparse_table[sparse_table[j][i-1]][i-1] # 희소 행렬[x][i]는 x에서 2**i번째 높이 위의 부모 노드

def query(u,v):
    '''u,v의 공통 부모를 반환하는 함수'''
    if depth[u]>depth[v]:
        u,v = v,u # u가 항상 높은 곳에 위치한다
    diff = depth[v] - depth[u]
    # 높이가 다르면 높이가 낮은 노드를 높이가 같아지도록 만든다 -> 노드의 높이 차이를 2의 지수로 분리하여 높이가 낮은 v를 업데이트 한다.
    while diff:
        t = diff & (-diff) # 최소 비트
        diff &= (diff-1) # 최소 비트 제거하기
        v = sparse_table[v][t.bit_length()] # 최소 비트의 위치로 업데이트

    # 높이가 같아졌는데도 u,v가 다르다면 u,v가 같아지는 노드를 찾는다
    while u!=v:
        for i in range(2,20): # 같아지기 직전으로 업데이트 해야 하고 최소 한번은 업데이트 해야 하기 때문에 2부터 시작하고 찾은 i에 1을 뺀 값을 이용한다
            if sparse_table[u][i] == sparse_table[v][i]:
                break
        u,v = sparse_table[u][i-1],sparse_table[v][i-1]
    return u

# 데이터를 입력받아 트리를 형성한다.
N = int(input())
tree = [[] for i in range(N+1)]
sparse_table = [[0]*20 for i in range(N+1)] # sparse_table[node][2**i위치의 노드]를 저장한다
parent = [0] * (N+1)
depth = [0] * (N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# 각 노드의 부모와 깊이를 계산한다.
find_parent(1,1)

# 희소 행렬을 구성한다.
make_sparse_table()

# 입력받은 쿼리를 처리한다
M = int(input())
for i in range(M):
    a,b = map(int,input().split())
    print(f'{query(a,b)}\n')

