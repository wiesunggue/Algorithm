import sys
input = sys.stdin.readline

H, W = map(int,input().split())
arr = [input().rstrip() for i in range(H)]

top = 0
bottom = H
left = 0
right = W
for i in range(H):
    if arr[i] != '.' * W:
        top = i
        break

for i in range(H-1,-1,-1):
    if arr[i] != '.' * W:
        bottom = i
        break

stop = False
for i in range(W):
    if stop:
        break
    for j in range(H):
        if arr[j][i] != '.':
            left = i
            stop = True
            break

stop = False
for i in range(W-1,-1,-1):
    if stop:
        break
    for j in range(H):
        if arr[j][i] != '.':
            right = i
            stop = True
            break

print(top, bottom)
print(left, right)

for i in range(top, bottom + 1):
    for j in range(left, right + 1):
        print(arr[i][j], end='')
    print()