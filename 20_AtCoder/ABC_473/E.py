N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = -1
ans = 0
psum = [arr[0]%K] * (N+1)
for i in range(1,N):
    psum[i] = arr[i] + psum[i-1]
    psum[i] %= K

hash = {}
hash[0] = -1


for i in range(N):
    if (hash.get(psum[i]) is not None) and hash[psum[i]] >= start:
        start = i
        ans += 1
    hash[psum[i]] = i

print(ans)