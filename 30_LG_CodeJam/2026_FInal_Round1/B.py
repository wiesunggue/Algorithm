L, N, K = map(int, input().split())
arr = list(map(int,input().split()))

m = arr[K-1]-arr[0]
for i in range(N-K+1):
    m = min(m, arr[K+i-1]-arr[i])
print(m)