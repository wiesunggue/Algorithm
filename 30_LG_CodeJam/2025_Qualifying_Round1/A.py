import sys
input = sys.stdin.readline
ORDER = [[1,1,1,1],[0,1,1,0],[1,1,0,0],[0,0,1,1],[1,0,0,1]]
def solve():
    N = int(input())
    SIZE = 100

    arr = [[[0] * 4 for _ in range(SIZE)] for _ in range(SIZE)]

    for _ in range(N):
        O, D, X, Y = map(int, input().split())

        if O == 1:  # x는 -방향, y는 +방향
            for x in range(X - D, X):
                for y in range(Y, Y + D):
                    distance = (X - 1 - x) + (y - Y)

                    if distance <= D - 2:
                        arr[x][y] = [1, 1, 1, 1]

                    elif distance == D - 1:
                        for t in range(4):
                            arr[x][y][t] |= ORDER[O][t]

        elif O == 2:  # x는 +방향, y는 +방향
            for x in range(X, X + D):
                for y in range(Y, Y + D):
                    distance = (x - X) + (y - Y)

                    if distance <= D - 2:
                        arr[x][y] = [1, 1, 1, 1]

                    elif distance == D - 1:
                        for t in range(4):
                            arr[x][y][t] |= ORDER[O][t]

        elif O == 3:  # x는 -방향, y는 -방향
            for x in range(X - D, X):
                for y in range(Y - D, Y):
                    distance = (X - 1 - x) + (Y - 1 - y)

                    if distance <= D - 2:
                        arr[x][y] = [1, 1, 1, 1]

                    elif distance == D - 1:
                        for t in range(4):
                            arr[x][y][t] |= ORDER[O][t]

        elif O == 4:  # x는 +방향, y는 -방향
            for x in range(X, X + D):
                for y in range(Y - D, Y):
                    distance = (x - X) + (Y - 1 - y)

                    if distance <= D - 2:
                        arr[x][y] = [1, 1, 1, 1]

                    elif distance == D - 1:
                        for t in range(4):
                            arr[x][y][t] |= ORDER[O][t]

    total = sum(value for row in arr for cell in row for value in cell) / 4
    print(f"{total:.2f}")


T = int(input())
for t in range(T):
    solve()