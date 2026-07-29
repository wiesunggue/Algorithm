# 탐색해야 하는 총 경우의 수
# 가로C2 * 세로C2, 가로 * 세로 = 10만
# 가로 5만 세로 2 => 5만 *2.5만 = 12.5억회 연산
# 1~9값인게 포인트
import bisect
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]

# 가로 세로 중 작은 걸 세자
if N > M:
    arr_temp = [[0]*N for i in range(M)]

    for i in range(N):
        for j in range(M):
            arr_temp[j][i] = arr[i][j]
    N, M = M, N
    arr = arr_temp

# 가로 방향 합
data = [0 for _ in range(20)]
ans = 0

for a1, a2 in combinations([i for i in range(N)], 2):
    data = [0 for _ in range(20)]
    # print(a1, a2,'-'*50)
    for k in range(M):
        data[arr[a1][k] + arr[a2][k]] += 1
    for i in range(2,10):
        ans += data[i] * data[20-i]
    ans += data[10] * (data[10]-1) // 2
print(ans)