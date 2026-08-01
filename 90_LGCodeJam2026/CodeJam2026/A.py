T = int(input())

def solve():
    N, K = map(int, input().split())
    arr = list(map(int,input().split()))
    result = float('inf')
    for k in range(K):
        ans = k
        before = arr[0] + k
        for i in range(1, N):
            if arr[i] <= before:
                cnt = before//K*K + before%K+1
                ans += cnt - arr[i]
                before = cnt
            else:
                cnt = (before % K-arr[i] % K + 1) % K
                before = arr[i] + cnt
                ans += cnt
        result = min(result, ans)
    print(result)


for test in range(T):
    solve()
