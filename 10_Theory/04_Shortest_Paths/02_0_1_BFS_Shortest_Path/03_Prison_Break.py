# 9376 탈옥 (Platinum IV)
# 다중 시작점 0-1 BFS, 거리 합성

# 문제 풀이
# 죄수 1(A)
# 죄수 2(B)
# 감옥 밖(O) 3개가 모두 연결되어야 함.
# 연결된다는 것은 특정 지점 P로부터 AP + BP + OP가 되고
# 각 AP, BP, OP가 최소가 되는 거리임.
# P를 미리 구할 수 없으므로 A, B, O에서 각각 이동 거리를 구한다.
# 임의의 P에 대해 세 거리 배열의 값을 합하면 AP + BP + OP가 된다.
# P가 문인 경우 문이 3번 계산되므로 세 이동 거리의 합에서 2를 빼야 한다.

from collections import deque


INF = float('inf')
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]


def zero_one_bfs(start, arr, w, h):
    dist = [[INF] * w for _ in range(h)]
    dq = deque([start])
    x, y = start
    dist[x][y] = 0

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if (
                not (0 <= next_x < h and 0 <= next_y < w)
                or arr[next_x][next_y] == '*'
            ):
                continue

            next_pos = (next_x, next_y)
            cost = dist[x][y] + int(arr[next_x][next_y] == '#')

            if cost < dist[next_x][next_y]:
                dist[next_x][next_y] = cost
                if arr[next_x][next_y] == '#':
                    dq.append(next_pos)
                else:
                    dq.appendleft(next_pos)

    return dist


def solution():
    h, w = map(int, input().split())
    arr = ['.' * (w + 2)]
    arr += ['.' + input() + '.' for _ in range(h)]
    arr += ['.' * (w + 2)]

    dist_arr = []
    for i in range(h + 2):
        for j in range(w + 2):
            if arr[i][j] == '$':
                dist_arr.append(zero_one_bfs((i, j), arr, w + 2, h + 2))

    dist_arr.append(zero_one_bfs((0, 0), arr, w + 2, h + 2))

    dist_total = [
        [0 if arr[j][i] != '#' else -2 for i in range(w + 2)]
        for j in range(h + 2)
    ]

    for i in range(h + 2):
        for j in range(w + 2):
            for d in range(3):
                dist_total[i][j] += dist_arr[d][i][j]

    answer = INF
    for i in range(h + 2):
        for j in range(w + 2):
            answer = min(answer, dist_total[i][j])

    print(answer)


T = int(input())
for _ in range(T):
    solution()
