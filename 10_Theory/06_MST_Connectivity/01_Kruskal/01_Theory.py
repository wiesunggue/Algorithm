"""
크루스칼 알고리즘(Kruskal)
=========================

연결된 무방향 가중치 그래프의 모든 정점을 최소 비용으로 연결하는
최소 신장 트리(MST)를 구한다.

신장 트리:
    모든 정점을 포함하고, 사이클이 없으며, 간선 수가 V - 1인 부분 그래프

절차:
    1) 모든 간선을 가중치 오름차순으로 정렬한다.
    2) 가장 가벼운 간선부터 확인한다.
    3) 양 끝 정점이 서로 다른 집합이면 간선을 선택하고 집합을 합친다.
    4) V - 1개를 선택하면 종료한다.

사이클 판별과 집합 병합에는 서로소 집합(Union-Find, DSU)을 사용한다.
경로 압축과 union by size/rank를 적용하면 연산 비용은 거의 상수이다.

시간 복잡도: O(E log E)
공간 복잡도: O(V + E)

주의:
- 방향 그래프의 MST에는 사용할 수 없다.
- 그래프가 연결되지 않으면 MST가 아니라 최소 신장 숲이 만들어진다.
- 음수 가중치도 사용할 수 있다.
- 동일 가중치가 있으면 MST가 여러 개일 수 있다.
"""


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True


def kruskal(vertex_count, edges):
    """
    edges의 원소는 (weight, u, v)이다.
    연결 그래프면 (최소 비용, 선택 간선)을, 아니면 (None, 선택 간선)을 반환한다.
    """
    dsu = DisjointSet(vertex_count)
    total_cost = 0
    selected = []

    for weight, u, v in sorted(edges):
        if dsu.union(u, v):
            total_cost += weight
            selected.append((weight, u, v))

            if len(selected) == vertex_count - 1:
                break

    if len(selected) != vertex_count - 1:
        return None, selected

    return total_cost, selected
