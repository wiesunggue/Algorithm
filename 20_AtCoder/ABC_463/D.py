import sys, bisect
input = sys.stdin.readline

N,K = map(int, input().split())
arr = [list(map(int,input().split())) for i in range(N)]
arr.sort(key= lambda x:x[1])
def binary_search():
    start = 0
    end = arr[-1][1]
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        print(start, mid, end)
        if count_cloths(mid) >= K:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans if ans != 0 else -1

def count_cloths(d):
    count = 1
    end = arr[0][1]
    for i in range(1,N):
        if end + d <= arr[i][0]:
            count += 1
            end = arr[i][1]

    return count

print(binary_search())

#print(count_cloths(35))