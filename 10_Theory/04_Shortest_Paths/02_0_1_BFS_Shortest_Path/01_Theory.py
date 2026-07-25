# 0-1 BFS 최단거리 알고리즘
# 다익스트라와 동일하지만 1인경우 Deque의 뒤쪽 삽입
# 0 인 경우 Deque의 앞에 삽입하여 정렬을 생략

from collections import deque

INF = float('inf')

def zero_one_bfs(start, graph, n):
    dist = [INF] * (n+1)
    dist[start] = 0

    dq = deque([start])

    while dq:
        current = dq.popleft()

        for next_node, weight in graph[current]:
            next_cost = weight + dist[current]

            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                if weight == 0:
                    dq.appendleft(next_node)
                else:
                    dq.append(next_node)


    return dist
