
N = int(input())
arr = []
for i in range(N):
    a,b = map(int, input().split())
    arr.append((min(a,b),max(a,b)))

arr.sort(key = lambda x: (x[0], x[1]))
print(*arr, sep ='\n')
min_y = arr[0][1]
ans = 1
for i in range(1, N):
    if arr[i][1] < min_y:
        min_y = arr[i][1]
        ans += 1


print(ans)