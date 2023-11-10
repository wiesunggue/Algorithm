# https://www.acmicpc.net/problem/9489
# 백준 9489번 사촌

N, K = map(int,input().split())
arr = list(map(int,input().split()))
tree = [[]for i in range(N)]

idx = 0
while idx<N:
    before = idx
    idx += 1
    while idx < N and arr[idx]-arr[idx-1] == 1:
        print(idx)
        idx += 1
        tree[before].append(idx)

print(tree)
