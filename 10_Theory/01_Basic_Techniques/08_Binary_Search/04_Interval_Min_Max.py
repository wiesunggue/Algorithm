# 기본 문제 2343번 기타 레슨
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 블루레이 사이즈에 대해서 이분탐색
def judge(size):
    cnt = 1
    total = 0
    for x in arr:
        if total + x > size:
            cnt += 1
            total = x
        else:
            total += x
    return cnt <= M

start = max(arr)
end = sum(arr)
while start <= end:
    mid = (start + end) // 2
    if judge(mid):
        end = mid - 1
    else:
        start = mid + 1
print(start)

# 응용 문제 13397번 구간 나누기 2
N, M = map(int, input().split())
arr = list(map(int, input().split()))

def judge(score):
    cnt = 1
    min_val = arr[0]
    max_val = arr[0]
    for i in range(N):
        min_val = min(min_val, arr[i])
        max_val = max(max_val, arr[i])
        if max_val - min_val > score:
            min_val = arr[i]
            max_val = arr[i]
            cnt += 1

    return cnt

# FFFFFTTTT 형태
start, end = 0, max(arr) - min(arr)
while start <= end:
    mid = (start + end) // 2
    if judge(mid) <= M:
        end = mid - 1
    else:
        start = mid + 1
print(start)

# 심화 문제 14421번 The Kingdom of JOIOI
