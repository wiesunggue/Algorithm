# https://www.acmicpc.net/problem/2696
# 백준 2696번 중앙값 찾기
import heapq
from collections import deque
# 아이디어
# 1. Max Heap 1, Min Heap 2를 선언
# 2. Heap 1에 값 저장
# 3. Heap 2는 Heap 1에 있는 값보다 클 때만 저장
# 4. 저장 후 개수가 다르다면 개수 조정하기

def solution():
    N = int(input())
    arr = []
    max_heap = []
    min_heap = []
    ans = deque()
    # 입력받기
    for i in range(N//10+1):
        arr += map(int,input().split())

    # 연산 및 결과 출력
    for i in range(N):
        # 힙에 넣기
        if i==0:# 초기값 채우기
            heapq.heappush(max_heap,-arr[i])
        elif -max_heap[0] > arr[i]:
            heapq.heappush(max_heap,-arr[i])
        else:
            heapq.heappush(min_heap,arr[i])
        #print(max_heap,min_heap)
        # 홀수 번째를 만나는 경우
        if i%2 == 0:
            # 두 힙간에 불균형이 있다면 조정한다
            while len(max_heap)-len(min_heap) != 1:
                #print(len(max_heap),len(min_heap))
                if len(max_heap)>len(min_heap):
                    heapq.heappush(min_heap,-heapq.heappop(max_heap))
                else:
                    heapq.heappush(max_heap,-heapq.heappop(min_heap))
            ans.append(-max_heap[0])
    n = len(ans)
    print(n)
    for i in range(n//10+1):
        for k in range(min(10,n-10*i)):
            print(ans[i*10+k],end=' ')
        print()

T = int(input())
for test in range(T):
    solution()
