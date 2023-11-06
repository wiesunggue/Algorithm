# https://www.acmicpc.net/problem/12764
# 백준 12764번 싸지방에 간 준하
import heapq
from collections import deque
import sys
input = sys.stdin.readline
# 시작시간 -> 정렬로 항상 시작시간이 증가하도록 구성
# 끝나는 시간 -> 우선순위 큐로 인덱스 접근
# 종료 -> 우선순위 큐를 통해서 종료된 컴퓨터를 다시 재할당

N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]
arr.sort()

data = [(arr[0][1],1)] # 우선순위큐에 의한 저장
computer = 1 # 저장할 컴퓨터의 개수
unalloc = [] # 중간에 사용 종료된 컴퓨터를 기록
ans = [0] * (N+1) # 컴퓨터 사용횟수 저장
ans[1] = 1 # 초기에 1번 컴퓨터 할당(arr[0]번)

for i in range(1,N):
    # 끝나는 시간이 먼저인 경우 제거 후 삽입한다
    while len(data):
        if data[0][0] < arr[i][0]:
            _,idx = heapq.heappop(data)
            heapq.heappush(unalloc,idx)
        else:
            break
    # 컴퓨터의 빈 공간이 존재할 때 빈 공간을 우선적으로 채운다
    if unalloc:
        idx=heapq.heappop(unalloc)
        heapq.heappush(data,(arr[i][1],idx))
        ans[idx] += 1
    # 빈 공간이 없다면 새 컴퓨터를 구매한다
    else:
        computer += 1
        heapq.heappush(data,(arr[i][1],computer))
        ans[computer] += 1

# 컴퓨터의 개수 출력
print(computer)

# 컴퓨터의 인덱스별 사용횟수 출력
print(*ans[1:computer+1])