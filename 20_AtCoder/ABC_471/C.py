N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
pos = 0
diff = float('inf')
for i in range(N):
    if abs(arr[i]) < diff:
        pos = i
        diff = abs(arr[i])
        ans = diff

print(arr)
print(pos)
iter = 1
posLeft = pos
posRight = pos
while iter < N:
    print(pos)
    iter += 1
    if posLeft == 0:
        ans += abs(arr[posRight+1] - arr[pos])
        pos = posRight + 1
        posRight = posRight + 1
    elif posRight == N-1:
        ans += abs(arr[posLeft-1] - arr[pos])
        pos = posLeft - 1
        posLeft = posLeft - 1
    elif posLeft==0 or (posRight != N and abs(arr[posLeft-1]-arr[pos]) > abs(arr[posRight+1]-arr[pos])):
        ans += abs(arr[posRight+1] - arr[pos])
        pos = posRight + 1
        posRight = posRight + 1
    else:
        ans += abs(arr[posLeft-1] - arr[pos])
        pos = posLeft - 1
        posLeft = posLeft - 1


print(ans)