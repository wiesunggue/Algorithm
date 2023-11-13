# https://www.acmicpc.net/problem/15900
# 백준 15900번 트리 탈출

# 리프 노드까지의 움직임이 짝수면 No 홀수면 Yes
import sys
sys.setrecursionlimit(500010)
input = sys.stdin.readline
def dfs(node):
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = visit[node] + 1
            dfs(n)

N = int(input())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)

for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

visit[1] = 1
dfs(1)
ans = 0
for i in range(1,N+1):
    if len(tree[i])==1:
        ans += visit[i] - 1

print('Yes' if ans%2!=0 else 'No')