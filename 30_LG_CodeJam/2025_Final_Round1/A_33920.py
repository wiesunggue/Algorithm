from collections import Counter

N, M = map(int, input().split())
D = list(map(int, input().split()))
C = list(map(int, input().split()))

D.sort()
cnt = Counter(D)
arr = sorted(cnt.items())


def bisect_right(arr, value, max_size):
    start, end = 0, max_size

    while start < end:
        mid = (start + end) // 2

        if arr[mid][0] <= value:
            start = mid + 1
        else:
            end = mid

    return start

result = []
max_size = len(arr)-1
for day in range(M):
    ans = 0
    left = bisect_right(arr, C[day]-day, max_size+1)

    cnt = 0
    print(arr)
    print('left',left, 'max_size',max_size)
    for j in range(left,max_size+1):
        print('iter',day,j,arr[j][0]-C[day]+day, arr[j][1])
        ans += max(0,arr[j][0]-C[day]+day)*arr[j][1]
        cnt += arr[j][1]
    if left <= max_size:
        if left != 0 and arr[left-1][0] == C[day]-day:
            left -= 1
            cnt += arr[left][1]
        max_size = left
        arr[max_size] = C[day]-day,cnt
    print(day, arr, left)
    result.append(str(ans))


print('\n'.join(result))