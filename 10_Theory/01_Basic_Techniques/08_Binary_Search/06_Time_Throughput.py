# 기본 문제 3079번 입국심사
N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

# K초간 처리할 수 있는 사람의 수 구하기
def count_people(time):
    total = 0
    for t in times:
        total += time // t
    return total

start, end = 1, max(times) * M
while start <= end:
    mid = (start + end) // 2
    if count_people(mid) >= M:
        end = mid - 1
    else:
        start = mid + 1

print(start)
# FFFFTTTTT

# 응용 문제 1561번 놀이 공원
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))

def count_people(time):
    total = 0
    for t in times:
        total += time // t + 1
    return total

start, end = 0, max(times) * N
while start <= end:
    mid = (start + end) // 2
    if count_people(mid) >= N:
        end = mid - 1
    else:
        start = mid + 1

count = count_people(start - 1)
for i in range(M):
    if start % times[i] == 0:
        count += 1
        if count == N:
            print(i + 1)
            break

# 심화 문제 1348번 주차장
