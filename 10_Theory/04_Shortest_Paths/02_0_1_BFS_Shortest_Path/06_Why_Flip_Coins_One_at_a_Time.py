# 20161 왜 동전은 하나씩만 뒤집는 거야 (Platinum IV)
# 비트마스크 상태 압축, BFS/DP 결합

# 아마 최대 그래프 depth가 제한이 있을 것 같음. (100 이하?)
# 최대 가능한 가지수는 2^100가지
# (N-K+1)*K개로 구성된 mask로 훑으면서 xor 연산을 진행(뒤집기)
#
from collections import deque

INF = float('inf')

N, K = map(int, input().split())
start = int(''.join(reversed(input().split())), 2)
target = int(''.join(reversed(input().split())), 2)
#start = 0
#target = (1<<N)-1

print('start', start)
print('target', target)
def bfs(start, target, N, K):
    mask = (1 << K) - 1

    idx = 0 # 왼쪽부터 확정된 coin의 위치
    dq = deque([(start, idx, 0)])
    dictionary = {}
    dictionary[(start, idx)] = 0
    while dq:
        now, idx, cost = dq.popleft()
        if dictionary.get((now, idx)) < cost:
            continue
        if target == now:
            return cost
        if idx+K < N and target & (1<<idx) == now & (1<<idx):
            if cost < dictionary.get((now, idx+1), INF):
                dictionary[(now, idx+1)] = cost
                dq.appendleft((now, idx+1, cost))
        m = mask << idx
        for i in range(K):

            next_m = m ^ 1<<(idx+i)

            if cost + 1 < dictionary.get((now ^ next_m, idx), INF):
                dq.append((now ^ next_m, idx, cost+1))
                dictionary[(now ^ next_m, idx)] = cost + 1


    return -1
print(bfs(start, target, N, K))