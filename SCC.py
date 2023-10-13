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
            
Test=input()
for test in Test:
    V, E = map(int, rinput().split())
    arr = [[] for i in range(V + 1)]
    reversed_arr = [[] for i in range(V + 1)]
    record = {i: [] for i in range(V + 1)}
    visit = [0] * (V + 1)
    st = deque()
    cnt = 0
    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        reversed_arr[b].append(a)

    for i in range(1, V + 1):
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
    for i in range(cnt):
        ans.append(sorted(record[i]))
    print(ans)
    ans.sort()
    print(cnt)
    for i in ans:
        for node in i:
            print(f"{node} ", end='')
        print('-1')
        