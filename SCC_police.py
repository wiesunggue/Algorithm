import sys
from collections import deque

# SCC 코사라주 구현 방식
# 1. 각 정점 마다 dfs
# 2. dfs 종료 시점에 스택에 각 정점 추가
# 3. 스택 순서로 역방향 dfs를 돌린다.
# 4. dfs로 방문 가능한 정점들이 하나의 SCC(종료될 때 까지)
sys.setrecursionlimit(10 ** 8)
rinput = sys.stdin.readline
rprint = sys.stdout.write


def dfs(node):
    for i in arr[node]:
        if visit[i] == 0:
            visit[i] = 1
            dfs(i)
    st.append(node)


def dfs2(node):
    global cnt
    for i in reversed_arr[node]:
        if visit[i] == 0:
            record[cnt].append(i)
            visit[i] = 1
            dfs2(i)

V = int(input())
arr = [[] for i in range(V + 1)]
reversed_arr = [[] for i in range(V + 1)]
record = {i: [] for i in range(V + 1)}
visit = [0] * (V + 1)
st = deque()
cnt = 0
cost = list(map(int, input().split()))
mat = [input() for i in range(V)]
for i in range(V):
    for j in range(V):
        if mat[i][j] == '1':
            arr[i].append(j)
            reversed_arr[j].append(i)

for i in range(V):
    if visit[i] == 0:
        visit[i] = 1
        dfs(i)

visit = [0] * (V + 1)
while st:
    node = st.pop()
    if visit[node] == 0:
        record[cnt].append(node)
        visit[node] = 1
        dfs2(node)
        cnt += 1
ans = []
Cost=0
for i in range(cnt):
    ans.append(sorted(record[i]))
print(ans)
for SCC in ans:
    minimum=10**9
    for scc in SCC:
        minimum=min(minimum,cost[scc])
    Cost+=minimum
print(Cost)