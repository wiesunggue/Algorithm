# https://www.acmicpc.net/problem/1655
# 백준 1655번 가운대를 말해요

# 전략
# 우선순위 큐를 2개 활용하여 중간값을 계속 유지하도록 선언
# MaxHeap에 하나를 저장하고 해당 값보다 작은 값이 온다면 maxHeap에 저장 크다면 minHeap에 저장
# ex) 5가 maxHeap에 저장된 상태에서 3이 온다면 maxHeap에 저장 maxHeap = [3,5], minHeap = []
# 데이터가 불균형한 상태가 되면 데이터를 균등하게 조정하는 연산을 실행(maxHeap의 제일 큰 값을 빼서 minHeap에 넣기) -> maxHeap = [3], minHeap = [5]로 조정
# 반대라면 minHeap의 제일 작은 값을 빼서 maxHeap에 넣는다.
# 해당 연산을 반복하면 maxHeap과 minHeap에 중앙값이 저장되게 된다.

import heapq
import sys
rinput = sys.stdin.readline
rprint = sys.stdout.write
max_heap = []
min_heap = []
def getmiddle(i,data):
    #print(i,data)
    if i == 0:
        heapq.heappush(max_heap,-data)
    # 데이터가 max_heap값 보다 큰 경우
    elif -max_heap[0] < data:
        heapq.heappush(min_heap,data)
    else:
        heapq.heappush(max_heap,-data)

    # 두개의 우선순위 큐의 사이즈 조정연산
    if i%2 == 0: # 홀수개의 데이터 저장
        while len(max_heap)-len(min_heap) != 1:
            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            else:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
    if i%2 == 1:
        while len(max_heap) != len(min_heap):
            if len(max_heap) < len(min_heap):
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            else:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
    #print(i,data, min_heap,max_heap)
    if i%2 == 0:
        return -max_heap[0]
    else:
        return min(-max_heap[0],min_heap[0])
N = int(input())
for i in range(N):
    print(f'{getmiddle(i,int(input()))}\n')