# 기본 문제 1300번 K번째 수
import bisect
N = int(input())
K = int(input())
arr = [i for i in range(1,N + 1)]
def count(x):
    # x 이하인 수의 개수를 반환
    total = 0
    for i in range(1, N + 1):
        total += bisect.bisect_right(arr, x/i) # Bisect를 굳이 할 필요는 없다.
        # x//i를 더해줘도 됨

    return total

start, end = 1, N * N
while start <= end:
    mid = (start + end) // 2
    if count(mid) >= K:
        end = mid - 1
    else:
        start = mid + 1
print(start)
# FFFFTTTT 이므로 start = T의 시작점

# 응용 문제 1637번 날카로운 눈
N = int(input())
arr = []
for i in range(N):
    A, C, B = map(int, input().split())
    arr.append((A, C, B))

def judge(x):
    # 1부터 x까지 출현한 개수를 반환하는 함수
    total = 0
    for i in range(N):
        A, C, B = arr[i]
        total += max(0, (min(C,x)-A)//B) + int(x>=A)
    return total

MAX_SIZE = 2147483647 + 1
start, end = 1, MAX_SIZE - 1
while start <= end:
    mid = (start + end) // 2
    if judge(mid) % 2 == 0:
        start = mid + 1
    else:
        end = mid - 1

if start != MAX_SIZE:
    print(start, judge(start)-judge(start-1)) # 첫번째로 홀수가 되는 지점
else:
    print("NOTHING")
# 심화 문제 12921번 제한된 메모리
