# https://www.acmicpc.net/problem/9489
# 백준 9489번 사촌

N, K = map(int,input().split())
arr = list(map(int,input().split()))
tree = [[]for i in range(N)]

nextSerial = 0
while nextSerial<N:
    before = nextSerial
    nextSerial += 1
    while nextSerial < N and arr[nextSerial]-arr[nextSerial - 1] == 1:
        print(nextSerial)
        nextSerial += 1
        tree[before].append(nextSerial)

print(tree)
