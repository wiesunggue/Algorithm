N, K = map(int, input().split())
arr = list(map(int, input().split()))

data = [0] * K
for i in range(N):
    data[arr[i]-1] += 1

m = max(data)
ans = 0
for i in range(K):
    if data[i] >= m-1:
        ans += 1

print(ans)