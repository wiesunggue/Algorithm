"""
이분 매칭(Bipartite Matching)
============================

정점을 서로 겹치지 않는 두 집합 L, R로 나눌 수 있고 모든 간선이 L과 R
사이를 연결하는 그래프에서, 정점을 중복 사용하지 않는 간선의 최대 집합을
찾는 문제이다.

예:
- 사람과 작업 배정
- 학생과 수업 배정
- 행과 열의 선택

DFS 기반 증가 경로 알고리즘:
    왼쪽 정점을 하나씩 보며 매칭을 시도한다.
    원하는 오른쪽 정점이 비어 있으면 바로 연결한다.
    이미 사용 중이면 기존 왼쪽 정점을 다른 곳으로 이동시킬 수 있는지
    재귀적으로 확인한다. 이렇게 매칭 수를 하나 늘리는 경로가 증가 경로다.

시간 복잡도: O(VE), 이분 그래프 표기로는 보통 O(|L|E)
큰 그래프에서는 O(E sqrt(V))인 Hopcroft-Karp를 고려한다.

쾨니그 정리:
    이분 그래프에서 최대 매칭 크기 = 최소 정점 커버 크기

주의:
- 한 번의 왼쪽 정점 탐색마다 visited를 새로 초기화한다.
- match_right[r]에는 r과 연결된 왼쪽 정점을 저장한다.
- 일반 그래프 매칭에는 이 알고리즘을 그대로 사용할 수 없다.
- 정점 번호 범위와 왼쪽/오른쪽 집합을 명확히 구분한다.
"""


def maximum_bipartite_matching(graph, right_size):
    """
    graph[left]에 연결 가능한 오른쪽 정점 번호가 들어 있다고 가정한다.
    최대 매칭 크기, 왼쪽 매칭, 오른쪽 매칭을 반환한다.
    """
    left_size = len(graph)
    match_right = [-1] * right_size

    def augment(left, visited):
        for right in graph[left]:
            if visited[right]:
                continue

            visited[right] = True
            if match_right[right] == -1 or augment(match_right[right], visited):
                match_right[right] = left
                return True

        return False

    matching_size = 0

    for left in range(left_size):
        visited = [False] * right_size
        if augment(left, visited):
            matching_size += 1

    match_left = [-1] * left_size
    for right, left in enumerate(match_right):
        if left != -1:
            match_left[left] = right

    return matching_size, match_left, match_right
