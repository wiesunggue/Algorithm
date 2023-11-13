# https://www.acmicpc.net/problem/20955
# 백준 20955번 민서의 응급 수술

# 문제 해결 전략
# 1. 연결된 그래프를 조사하여 끊어서 트리를 만든다(dfs에서 중복 접근을 하지 못할 때 탐색을 못한 횟수) - 왔다갔다 하는 경우를 제거하기 위해서 딕셔너리 사용
# 2. 연결되지 않은 트리의 개수 = 합쳐야 할 횟수로 본다(dfs함수의 시작 횟수)

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**5+1)
def dfs(node):
    global break_node
    for n in tree[node]:
        if visit[n] != 1:
            visit[n] = 1
            used[(node,n)] = 1
            used[(n,node)] = 1
            dfs(n)
        elif used[(node,n)] == 0:
            break_node += 1

# 그래프 입력 받기
N,M = map(int,input().split())
tree = [[] for i in range(N+1)]
used = defaultdict(int)
visit = [0] * (N + 1)
for i in range(M):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

break_node = 0
not_connected = -1 # 1개의 그래프만 존재하면 0번 합쳐야 한다

for i in range(1,N+1):
    if visit[i] == 1:
        continue
    visit[i] = 1
    dfs(i)
    not_connected += 1

print(break_node//2+not_connected)