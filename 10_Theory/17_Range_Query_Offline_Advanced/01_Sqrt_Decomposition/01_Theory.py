'''
Sqrt Decomposition 대표 예제
구간 합, 최솟값, 최댓값 계산
구간 갱신 + 점 질의
구간 갱신 + 구간 합 질의
구간에서 x이하, 이상 개수 세기
구간 K번째 수
블록 Lazy를 활용한 정렬된 블록 문제
동적 배열: 삽입 / 삭제 / K번째 접근
주기적 재빌드 / Batch Processing 

'''

class SqrtDecomposition:
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = arr

        self.B = int(self.N ** 0.5) + 1

        self.num_blocks = (self.N + self.B - 1) // self.B
        self.block_sum = [0] * self.num_blocks

        for i, value in enumerate(self.arr):
            b = i // self.B
            self.block_sum[b] += value

    def update(self, idx, value):
        b = idx // self.B

        self.block_sum[b] -= self.arr[idx]
        self.arr[idx] = value
        self.block_sum[b] += value
    
    def query(self, left, right):
        result = 0
        
        start_block = left // self.B
        end_block = right // self.B

        if start_block == end_block:
            for i in range(left, right + 1):
                result += self.arr[i]
            return result
        
        left_end = (start_block + 1) * self.B -1
        for i in range(left, min(left_end, self.N-1)+1):
            result += self.arr[i]

        for b in range(start_block + 1, end_block):
            result += self.block_sum[b]
        
        right_start = end_block * self.B
        for i in range(right_start, right + 1):
            result += self.arr[i]
        
        return result
    