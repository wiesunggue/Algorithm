# 벨만 포드 알고리즘
# 시작점에서 table 위치까지 최단거리 찾기 알고리즘

INF = float('inf')

def bellman_ford(start, n, edges):
    dist = [INF] * (n+1)
    dist[start] = 0

    for i in range(1, n+1):
        updated = False

        for u, v, weight in edges:
            if dist[u] == INF:
                continue

            next_dist = dist[u] + weight

            if next_dist < dist[v]:
                dist[v] = next_dist
                updated = True

                if i == n:
                    return None

        if not updated:
            break

    return dist


# Bellman Ford 대표적인 응용 방식
# 1. 최고 Cost 찾기 -> 음수 가중치 가지는 경우와 동일함
# 2. 경로간 곱셈 문제 -> log를 활용한 곱셈 <-> 덧셈 변환 활용
# 3. 다중 시작점 문제 -> 모든 시작점 위치에 0 대입하여 연산
# 4. 음수 사이클의 존재 여부 탐색 -> 초기 시작 dist = [0]*(N+1)으로 두고 탐색 진행
# 5. 한 번 탐색해서 완화하는 방법에 따라 탐색 횟수 차이가 발생함
# 6. 최단 경로에 포함되는 간선은 N-1개의 간선이 됨(dist[k][v], k는 간선의 개수, v는 노드) -> N번째 갱신된 경우 음수 사이클이 있다고 볼 수 있음(dist[N][v] < dist[N-1][v])
# 7. 갱신된 정점만 우선적으로 처리하는 최적화(갱신 안된 경우에는 탐색 필요x) -> 갱신이 일어나지 않은 정점의 비교는 동일한 비교가 됨 -> SPFA의 아이디어

