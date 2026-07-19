from collections import defaultdict,deque

N, K, M = map(int, input().split())


gems = [list(map(int,input().split())) for i in range(N)]

gems.sort(key=lambda x: -x[1])

d = defaultdict(int)
dq = deque()
for i in range(K):
    d[gems[i][0]] += 1
    if d[gems[i][0]] >= 2:
        dq.append(i)

print(d)
