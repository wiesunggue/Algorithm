N, Q = map(int, input().split())

L = [i for i in range(N)]
R = list(map(int, input().split()))
for i in range(N):
    R[i] -= 1
state = 0
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1] - 1, query[2] - 1
        if state % 2 == 0:
            R[a], R[b] = R[b], R[a]
        else:
            L[a], L[b] = L[b], L[a]
    if query[0] == 2:
        state += 1


ans = []
inv = [0] * N
print(L)
print(R)
if state % 2 == 0:
    for i in range(N):
        inv[L[i]] = i
    for i in range(N):
        ans.append(str(inv[R[i]]+1))
    print(' '.join(ans))

else:
    for i in range(N):
        inv[R[i]] = i
    for i in range(N):
        ans.append(str(inv[L[i]]+1))
    print(' '.join(ans))