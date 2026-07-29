"""
SCC(Strongly Connected Component, 강한 연결 요소)
================================================

방향 그래프에서 서로 왕복 가능한 정점들의 최대 집합이다.
같은 SCC 안의 임의의 두 정점 u, v에 대해 u -> v와 v -> u 경로가 모두
존재한다.

SCC를 각각 하나의 정점으로 압축하면 항상 DAG가 된다. 이 압축 그래프는
사이클 의존성을 묶거나 2-SAT, 도달 가능성, 최소 시작점 문제 등에 쓰인다.

대표 알고리즘:
- 코사라주: 원본 그래프 DFS 종료 순서 + 역방향 그래프 DFS
- 타잔: DFS 한 번에서 발견 순서와 low-link를 관리

코사라주 절차:
    1) 원본 그래프 DFS가 끝나는 순서대로 정점을 기록한다.
    2) 간선을 모두 뒤집은 그래프를 만든다.
    3) 종료 순서의 역순으로 역그래프 DFS를 한다.
    4) 한 번의 DFS에서 방문한 정점들이 하나의 SCC이다.

시간 복잡도: O(V + E)
공간 복잡도: O(V + E)

주의:
- 무방향 그래프의 연결 요소와 다르다.
- 첫 DFS의 종료 순서가 중요하다.
- 압축 그래프를 만들 때 같은 SCC 내부 간선은 제거한다.
- 재귀 DFS는 정점 수가 크면 재귀 제한 또는 반복 DFS를 고려한다.
"""


def strongly_connected_components(graph):
    """코사라주 알고리즘으로 SCC 목록과 각 정점의 SCC 번호를 반환한다."""
    n = len(graph)
    reverse_graph = [[] for _ in range(n)]

    for node in range(n):
        for neighbor in graph[node]:
            reverse_graph[neighbor].append(node)

    visited = [False] * n
    order = []

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        order.append(node)

    for node in range(n):
        if not visited[node]:
            dfs(node)

    component_id = [-1] * n
    components = []

    def reverse_dfs(node, identifier):
        component_id[node] = identifier
        components[identifier].append(node)

        for neighbor in reverse_graph[node]:
            if component_id[neighbor] == -1:
                reverse_dfs(neighbor, identifier)

    for node in reversed(order):
        if component_id[node] == -1:
            components.append([])
            reverse_dfs(node, len(components) - 1)

    return components, component_id


def condensation_graph(graph):
    """SCC를 정점으로 압축한 DAG를 인접 집합 형태로 반환한다."""
    components, component_id = strongly_connected_components(graph)
    dag = [set() for _ in components]

    for node in range(len(graph)):
        for neighbor in graph[node]:
            current = component_id[node]
            following = component_id[neighbor]
            if current != following:
                dag[current].add(following)

    return dag, components, component_id
