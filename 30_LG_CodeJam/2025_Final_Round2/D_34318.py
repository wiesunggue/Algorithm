import sys
input = sys.stdin.buffer.readline

N, C = map(int, input().split())

# 시각을 0~11로 변환
D = [x - 1 for x in map(int, input().split())]
W = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append(b)
    graph[b].append(a)


# 1. 트리를 0번 정점 기준으로 루팅
parent = [-1] * N
order = [0]

for u in order:
    for v in graph[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        order.append(v)


# dp[u][t]
# u가 포함된 연결 요소가 원래 t시였던 시계들을
# 12시로 맞추도록 회전할 때, u 서브트리에서 얻는 최대 이익
dp = [[0] * 12 for _ in range(N)]


# 2. 자식부터 계산하는 후위 순회
for u in reversed(order):
    current = dp[u]

    # 정점 u 자체의 보상
    current[D[u]] = W[u]

    # 각 자식 서브트리를 현재 정점에 병합
    for v in graph[u]:
        if parent[v] != u:
            continue

        child = dp[v]

        # u-v 간선을 자르는 경우
        # 자식 컴포넌트는 원하는 시각을 독립적으로 선택 가능
        disconnected = max(child) - C

        for t in range(12):
            # u-v 간선을 유지하는 경우:
            # 부모와 자식이 같은 컴포넌트이므로 같은 t를 선택
            connected = child[t]

            current[t] += max(connected, disconnected)


# 루트는 부모와 연결될 필요가 없으므로
# 12개 상태 중 자유롭게 최댓값 선택
print(max(dp[0]))