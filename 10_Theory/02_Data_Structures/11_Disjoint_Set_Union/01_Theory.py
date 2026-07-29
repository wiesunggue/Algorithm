"""
Union-Find / DSU(Disjoint Set Union, 서로소 집합)
================================================

서로 겹치지 않는 여러 집합을 관리하면서 다음 두 연산을 빠르게 처리하는
자료구조이다.

- find(x): x가 속한 집합의 대표 원소(root)를 찾는다.
- union(a, b): a와 b가 속한 두 집합을 하나로 합친다.

두 원소가 같은 집합에 속하는지는 find(a) == find(b)로 확인한다.


1. 트리 표현
------------
각 집합을 하나의 트리로 표현한다.

parent[x] = x:
    x가 해당 집합의 대표 원소이다.

parent[x] != x:
    x의 부모가 parent[x]이다.

find 연산은 부모를 따라 루트까지 올라간다. union 연산은 두 루트를 찾아
한 루트를 다른 루트의 자식으로 만든다.


2. 경로 압축(Path Compression)
------------------------------
find(x)를 실행하면서 경로에 있는 모든 정점의 부모를 루트로 바꾼다.
이후 같은 정점들에 대한 find 연산이 매우 빨라진다.

    parent[x] = find(parent[x])


3. Union by Size / Rank
-----------------------
작은 트리를 큰 트리 아래에 붙인다. 트리 높이가 불필요하게 커지는 것을
막아 find 연산을 빠르게 유지한다.

- size: 집합에 포함된 원소 개수를 기준으로 병합
- rank: 트리 높이의 상한을 기준으로 병합

경로 압축과 union by size/rank를 함께 사용하면 M번의 연산 시간은
O(M * alpha(N))이다. alpha는 역 아커만 함수이며 현실적인 입력 범위에서
5보다 작으므로 연산당 거의 O(1)로 본다.


4. 활용
-------
- 무방향 그래프의 연결 여부 확인
- 사이클 판별
- 크루스칼 최소 신장 트리
- 연결 요소 개수와 각 요소의 크기 관리
- 오프라인 질의 처리
- 같은 그룹에 속해야 한다는 동치 관계 관리


5. 사이클 판별
--------------
무방향 그래프에서 간선 (u, v)를 추가할 때:

    find(u) == find(v):
        이미 같은 연결 요소이므로 이 간선을 추가하면 사이클이 생긴다.

    find(u) != find(v):
        서로 다른 연결 요소이므로 union(u, v)로 합친다.

방향 그래프의 일반적인 사이클 판별에는 Union-Find를 사용할 수 없다.


6. 실수하기 쉬운 점
-------------------
- union할 때 원소 자체가 아니라 두 원소의 루트를 연결해야 한다.
- size는 루트에서만 유효하도록 관리한다.
- 정점 번호가 1부터 시작하면 배열 크기를 N + 1로 만든다.
- 일반 DSU는 간선 삭제나 집합 분리를 지원하지 않는다.
- Rollback DSU에서는 변경 이력을 복원해야 하므로 보통 경로 압축을 쓰지
  않고 union by size만 사용한다.
- 대표 원소 번호에는 특별한 의미가 없으며, 병합 순서에 따라 달라진다.
"""


class DisjointSetUnion:
    """경로 압축과 union by size를 사용하는 Union-Find."""

    def __init__(self, size):
        self.parent = list(range(size))
        self.component_size = [1] * size
        self.component_count = size

    def find(self, node):
        """node가 속한 집합의 대표 원소를 반환한다."""
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        """
        a와 b의 집합을 합친다.
        실제로 합쳐졌으면 True, 이미 같은 집합이면 False를 반환한다.
        """
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        # 항상 작은 트리를 큰 트리 아래에 붙인다.
        if self.component_size[root_a] < self.component_size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.component_size[root_a] += self.component_size[root_b]
        self.component_count -= 1
        return True

    def same(self, a, b):
        """a와 b가 같은 집합에 속하는지 반환한다."""
        return self.find(a) == self.find(b)

    def size(self, node):
        """node가 속한 집합의 원소 개수를 반환한다."""
        return self.component_size[self.find(node)]

    def groups(self):
        """현재 집합들을 {대표 원소: [원소들]} 형태로 반환한다."""
        result = {}

        for node in range(len(self.parent)):
            root = self.find(node)
            result.setdefault(root, []).append(node)

        return result


def contains_cycle(vertex_count, edges):
    """무방향 그래프가 사이클을 포함하는지 Union-Find로 판별한다."""
    dsu = DisjointSetUnion(vertex_count)

    for u, v in edges:
        if not dsu.union(u, v):
            return True

    return False
