import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, C = map(int, input().split())
D = list(map(int, input().split()))
W = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

postorder = []
parent = [0]*(N+1)
visited = [False] * (N + 1)
visited[1] = True
dp = [[0]*12 for _ in range(N + 1)]

# 후위 순회
def dfs(node):
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            parent[i] = node
            dfs(i)
    dp[node][D[node-1]%12] = W[node-1]
    postorder.append(node)

dfs(1)

for i in range(N):
    c = postorder[i]
    p = parent[c]
    for t in range(12):
        dp[p][t] += max(dp[c][t], max(dp[c])-C)

print(max(dp[1]))