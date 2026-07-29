"""
위상 정렬(Topological Sort)
==========================

방향 그래프의 모든 간선 u -> v에 대해 u가 v보다 먼저 나오도록 정점을
나열하는 방법이다. 위상 정렬은 DAG(Directed Acyclic Graph)에서만 모든
정점을 포함할 수 있다.

활용:
- 선수 과목과 작업 순서
- 빌드 의존성
- DAG 동적 계획법
- 순서 관계의 모순 판별

칸 알고리즘(Kahn's Algorithm):
    1) 모든 정점의 진입 차수를 계산한다.
    2) 진입 차수가 0인 정점을 큐에 넣는다.
    3) 큐에서 정점을 꺼내 결과에 추가한다.
    4) 나가는 간선을 제거한 효과로 이웃의 진입 차수를 1 줄인다.
    5) 새로 0이 된 정점을 큐에 넣는다.

결과 정점 수가 V보다 작으면 사이클이 존재한다.

시간 복잡도: O(V + E)
공간 복잡도: O(V + E)

특징:
- 위상 순서는 여러 개일 수 있다.
- 사전순 최소 결과가 필요하면 큐 대신 최소 힙을 사용한다.
- 처리 중 선택 가능한 정점이 2개 이상이면 순서가 유일하지 않다.
- DFS 종료 순서를 뒤집는 방법도 있지만 사이클 검사를 별도로 해야 한다.
"""

from collections import deque
import heapq


def topological_sort(graph):
    """위상 순서를 반환하고, 사이클이 있으면 빈 리스트를 반환한다."""
    n = len(graph)
    indegree = [0] * n

    for node in range(n):
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque(node for node in range(n) if indegree[node] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == n else []


def lexicographical_topological_sort(graph):
    """가능한 위상 순서 중 정점 번호가 사전순으로 가장 작은 것을 반환한다."""
    n = len(graph)
    indegree = [0] * n

    for node in range(n):
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    heap = [node for node in range(n) if indegree[node] == 0]
    heapq.heapify(heap)
    order = []

    while heap:
        node = heapq.heappop(heap)
        order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    return order if len(order) == n else []
