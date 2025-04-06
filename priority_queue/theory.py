# 23. 우선순위 큐와 힙

# 힙 - 항상 상위 노드가 큰 값을 가지는 틜
# 힙이 효율적이기 위한 제약
# 1. 마지막 레벨을 제외한 모든 레벨에 노드가 꽉 차 있어야 한다
# 2. 마지막 레벨에 노드가 있을 때는 항상 왼쪽부터 순서대로 채워야 한다.
# => 힙의 높이는 O(lgN)

class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push_heap(self,value):
        self.heap.append(value)
        idx = self.size
        self.size = self.size+1

        while(idx>0 and self.heap[(idx-1)//2] < self.heap[idx]):
            self.heap[idx], self.heap[(idx-1)//2] = self.heap[(idx-1)//2],self.heap[idx]
            idx = (idx-1)//2

    def pop_heap(self):
        max_value = self.heap[0]
        self.heap.pop(0)
        self.size -= 1
        here = 0
        while(1):
            left,right = here*2+1, here*2+2
            if(left>=self.size): break
            next = here
            if(self.heap[next] < self.heap[left]):
                next = left
            if(right<self.size and self.heap[next] < self.heap[right]):
                next = right
            if(next==here): break
            self.heap[here],self.heap[next] = self.heap[next],self.heap[here]
            here = next
        return max_value

h = Heap()
for i in range(10):
    h.push_heap(i)

for i in range(10):
    print(h.pop_heap())


# 중앙값 찾기
# 중앙값 찾기 위해서는 힙을 2개 이용한다.
# 최소 힙, 최대 힙
# 최대 힙은 최소 힙보다 항상 작아야 한다.
# 최대 힙이 개수가 최소 힙보다 1개 더 많거나 같도록 유지하면 항상 중앙값을 찾을 수 있다.
