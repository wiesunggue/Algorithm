# 기본 문제 1981번 배열에서 이동
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

def bfs(start, end):
    if not start <= arr[N-1][N-1] <= end or not start<= arr[0][0] <= end:
        return False
    dq = deque()
    dq.append((0,0))
    visit = [[0] * N for _ in range(N)]
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            new_x, new_y = x + move_x[i], y + move_y[i]
            if 0 <= new_x < N and 0 <= new_y < N and visit[new_x][new_y] == 0 and start <= arr[new_x][new_y] <= end:
                if new_x == N-1 and new_y == N-1:
                    return True

                visit[new_x][new_y] = visit[x][y] + 1
                dq.append((new_x, new_y))

    if visit[N-1][N-1] != 0:
        return True
    else:
        return False
def judge(k):
    for i in range(200-k):
        print(i, i+k)
        if bfs(i, i+k):
            return True
    return False

start, end = 0, 200
while start <= end:
    mid = (start + end) // 2
    if judge(mid):
        end = mid - 1
    else:
        start = mid + 1
print(start)

# 응용 문제 2842번 집배원 한상덕
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

move_x = [0, 0, -1, -1, -1, 1, 1, 1]
move_y = [-1, 1, -1, 0, 1, -1, 0, 1]
MAX_SIZE = 1000000
data = set()
pos = [input() for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
house = 0
for i in range(N):
    for j in range(N):
        if pos[i][j] == 'K':
            house += 1

        if pos[i][j] == 'P':
            P = (i,j)
        data.add(arr[i][j])
data = list(data)
data.sort()
def bfs(start, end):
    if not start <= arr[P[0]][P[1]] <= end:
        return False

    dq = deque()
    dq.append(P)
    visit = [[0] * N for _ in range(N)]
    visit[P[0]][P[1]] = 1
    cnt = 0
    while dq:
        x, y = dq.popleft()
        for i in range(8):
            new_x, new_y = x + move_x[i], y + move_y[i]
            if 0 <= new_x < N and 0 <= new_y < N and visit[new_x][new_y] == 0 and start <= arr[new_x][new_y] <= end:
                visit[new_x][new_y] = visit[x][y] + 1
                dq.append((new_x, new_y))
                if pos[new_x][new_y] == 'K':
                    cnt += 1
                if cnt == house:
                    return True

    return False


def judge():
    start, end = 0, 0
    m = float('inf')
    while end < len(data) and start <= end:
        print(start, end)
        if bfs(data[start], data[end]) == False:
            end += 1
        else:
            m = min(m, abs(data[end] - data[start]))
            start += 1

    return m

print(judge())

# 심화 문제 10227번 삶의 질

