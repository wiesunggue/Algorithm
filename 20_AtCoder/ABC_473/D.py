import sys

print = sys.stdout.write
N, K = map(int, input().split())

arr = [0] * N
ans = []
def recur(idx, arr, total):
    if idx == N - 2:
        if (K-total) % N == 0:
            arr[N-1] = (K-total)//N
            ans.append(arr.copy())
        return

    t = total
    i = idx + 1
    while t<=K:
        recur(i, arr, t)
        arr[i] += 1
        t += i+1
    arr[i] = 0
recur(-1, arr, 0)

result = []
for i in range(len(ans)):
    result.append(' '.join(map(str,ans[i])))

print('\n'.join(result))
