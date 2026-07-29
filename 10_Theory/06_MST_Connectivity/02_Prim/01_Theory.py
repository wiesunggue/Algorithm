"""
프림 알고리즘(Prim)
==================

연결된 무방향 가중치 그래프의 최소 신장 트리(MST)를 구한다.
하나의 시작 정점에서 출발하여 현재 트리와 바깥 정점을 연결하는 간선 중
가장 가벼운 것을 반복해서 선택한다.

절차:
    1) 시작 정점과 비용 0을 최소 힙에 넣는다.
    2) 힙에서 비용이 가장 작은 간선을 꺼낸다.
    3) 도착 정점이 이미 트리에 포함되었다면 건너뛴다.
    4) 아니라면 정점과 간선을 트리에 포함한다.
    5) 새 정점에서 나가는 간선을 힙에 넣는다.

인접 리스트 + 최소 힙:
    시간 복잡도 O(E log V), 공간 복잡도 O(V + E)

크루스칼과 비교:
- 크루스칼: 간선 중심, 전체 간선 정렬, Union-Find 사용
- 프림: 정점 확장 중심, 현재 경계의 간선만 힙으로 관리
- 희소 그래프에서는 둘 다 효율적이며 구현과 입력 형태에 따라 선택한다.

주의:
- 우선순위 큐에는 정점이 아니라 해당 정점으로 들어가는 간선 비용을 넣는다.
- 이미 방문한 정점으로 향하는 오래된 힙 항목을 건너뛴다.
- 그래프가 연결되지 않으면 모든 정점을 방문할 수 없다.
- 시작 정점이 달라도 MST 총비용은 같지만 선택 간선은 달라질 수 있다.
"""

import heapq


def prim(graph, start=0):
    """
    graph[u]의 원소는 (weight, v)이다.
    연결 그래프면 (최소 비용, 선택 간선)을, 아니면 (None, 선택 간선)을 반환한다.
    """
    n = len(graph)
    if n == 0:
        return 0, []

    visited = [False] * n
    # (간선 비용, 현재 정점, 부모 정점)
    heap = [(0, start, -1)]
    total_cost = 0
    selected = []
    visited_count = 0

    while heap and visited_count < n:
        weight, node, parent = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        visited_count += 1
        total_cost += weight

        if parent != -1:
            selected.append((weight, parent, node))

        for next_weight, neighbor in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(heap, (next_weight, neighbor, node))

    if visited_count != n:
        return None, selected

    return total_cost, selected
