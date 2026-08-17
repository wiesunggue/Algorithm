# 기본 문제 2110번 공유기 설치
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
# mindist 를 maximize 하는 문제
def judge(mindist):
    cnt = 1
    last = arr[0]
    for i in range(1, N):
        if arr[i] - last >= mindist:
            cnt += 1
            last = arr[i]
    return cnt >= C

start, end = 1, arr[-1]
while start <= end:
    mid = (start + end) // 2
    if judge(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)
# TTTTFFFF 인 형태 -> start = F인 최솟 값, end = T인 최댓 값


# 응용 문제 6209번 제자리 멀리뛰기
d, n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

# dist가 k 미만이면 삭제하기
def judge(k):
    cnt = 0
    last = 0
    for i in range(n):
        if arr[i] - last < k:
            cnt += 1
        else:
            last = arr[i]
    if d - arr[-1] < k:
        cnt += 1
    return cnt <= m

# TTTTFFFF
start, end = 0, d
while start <= end:
    mid = (start + end) // 2
    if judge(mid):
        end = mid - 1
    else:
        start = mid + 1

print(end)
# 심화 문제 17976번 Thread Knots
