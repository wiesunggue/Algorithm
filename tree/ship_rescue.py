# https://www.acmicpc.net/problem/16437
# 백준 16437번 양 구출 대작전 문제

import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

# 트리 만들기
N = int(input())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
weight = [0] * (N+1)
for i in range(1,N):
    t,a,p = input().split()
    a,p = int(a),int(p)
    tree[i+1].append((p))
    tree[p].append((i+1))
    weight[i+1] = a if t=='S' else -a
def dfs(node):
    '''dfs를 활용해서 탐색 종료 시 값을 더하고 max(총 합+weight[node],0)을 반환하는 함수'''
    m = 0
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            m += dfs(n)
    return max(m+weight[node],0)

visit[1] = 1
print(dfs(1))