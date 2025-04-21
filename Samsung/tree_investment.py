# https://www.acmicpc.net/problem/16235
# 나무 제테크
import sys
from collections import deque
input = sys.stdin.readline

nearly = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
N, M, K = map(int, input().split())

nutrients = [[5] * N for i in range(N)]
tree_age = []
arr = [list(map(int, input().split())) for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    tree_age.append((a - 1, b - 1, c))

tree_age.sort(key=lambda x: x[2])
tree_age = deque(tree_age)
for i in range(K):
    # spring
    new_tree = deque()
    dead_tree = deque()
    while tree_age:
        a, b, c = tree_age.popleft()
        if c <= nutrients[a][b]:
            new_tree.append((a, b, c + 1))
            nutrients[a][b] -= c
        else:
            dead_tree.append((a, b, c))

    tree_age = new_tree

    # summer
    while dead_tree:
        a, b, c = dead_tree.popleft()
        nutrients[a][b] += c // 2

    # fall
    fall_tree = deque()
    while tree_age:
        a, b, c = tree_age.popleft()
        if c % 5 == 0:
            for near in nearly:
                na, nb = a + near[0], b + near[1]
                if 0 <= na < N and 0 <= nb < N:
                    fall_tree.appendleft((na, nb, 1))
        fall_tree.append((a,b,c))

    # winter
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += arr[i][j]
    tree_age = fall_tree

print(len(tree_age))