# 기본 문제 1654번 랜선 자르기
import sys
from turtle import pos
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid

    if cnt >= K:
        start = mid + 1
    else:
        end = mid - 1
print(end)


# 응용 문제 1114번 통나무 자르기
import sys
import bisect
input = sys.stdin.readline

L, K, C = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def possible(x):
    # 최대 길이가 x인 통나무로 자를 수 있는지 확인하는 함수
    last = L
    for cnt in range(C):
        # arr에서 last - x 이상인 값 찾기
        idx = bisect.bisect_left(arr, last - x)
        if idx == K:
            return False, -1
        last = arr[idx]
    if last > x:
        return False, -1
    return True, last

start = 1
end = L
while start <= end:
    mid = (start + end) // 2
    p, f = possible(mid)
    if not p:
        start = mid + 1
    else:
        end = mid - 1

print(start, possible(start)[1])

# 심화 문제 5530번 JOIOI 탑
N = (int(input()))
s = input()

# JOI 혹은  IOI로 만드는 경우
