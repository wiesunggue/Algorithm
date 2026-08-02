import heapq

N = int(input())
position = []
for i in range(N):
    a, b, w = map(int, input().split())
    position.append((min(a,b), max(a,b), w))
C = list(map(int, input().split()))

position.sort()
base = [0] * N
for i in range(N):
    base[i] = position[i][2] * (position[i][1] - position[i][0])
max_base = max(base)


def parametric(X):
    # 반드시 불가능한 경우
    if X < max_base:
        return False

    D = [0] * N
    range_arr = []

    for i in range(N):
        # 가능한 구간 찾기
        D[i] = (X - base[i])//(2*position[i][2])

        start = position[i][0] - D[i]
        end = position[i][1] + D[i]

        range_arr.append((start, end))

    range_arr.sort()

    pq = []
    j = 0
    for i in range(N):
        while j<N and range_arr[j][0] <= C[i]:
            heapq.heappush(pq, (range_arr[j][1], range_arr[j][0]))
            j+=1
        if not pq:
            return False
        if C[i] > heapq.heappop(pq)[0]:
            return False # 범위 안에 안 들어가는 경우

    return True

l, r = 0, 10**15+1
for i in range(52):
    mid = (l+r)//2
    if parametric(mid):
        r = mid
    else:
        l = mid + 1

print(l)