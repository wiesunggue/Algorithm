'''Range Query의 경우 다음과 같은 연산이 가능하다
1. Max Query + Range Add
2. Max Query + Range Assign
3. Range Sum + Range Assign
4. Range Sum + Range Assign + Range Add
5. Range Sum + Range Multiply
6. Range Sum + Range Affine
7. Range XOR + Range XOR
8. Range Sum + Range XOR
9. First Position Query(k이상인 수 중 가장 왼쪽) + Range Add
10. Range Sum of Square + Range Add
11. Range GCD + Range Add
'''

import sys
sys.setrecursionlimit(10**5)

class RecursivLazySegmentTree:
    '''1. Max Query와 Range Add Update Query 를 가진 세그먼트 트리'''
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = arr
        self.size = 1

        while self.size < self.N:
            self.size *= 2
        
        self.tree = [-10**10] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)
        self.haslazy = [False] * (2 * self.size)

        self._build(1,0,self.N-1)
    def _build(self, node, left, right):
        if left == right:
            self.tree[node] = self.arr[left]
            return self.tree[node]
        
        mid = (left + right) // 2
        self.tree[node] = max(self._build(node*2,left,mid),self._build(node*2+1,mid+1,right))
        return self.tree[node]

    def _query(self, node, left, right, l, r):
        if right<l or r < left:
            return -10**10
        
        if l<=left and right<=r:
            return self.tree[node]
        
        self._push(node, left, right)
        mid = (left + right) // 2
        return max(self._query(node*2, left, mid,l,r), self._query(node*2+1, mid+1, right,l,r))
    
    def _update(self, node, left, right, l, r, value):
        if right<l or r < left:
            return 
        
        if l<=left and right<=r:
            self._apply(node, left, right, value)
            return 

        self._push(node, left, right)
        mid = (left + right) // 2
        self._update(node*2,left,mid,l,r,value)
        self._update(node*2+1,mid+1,right,l,r,value)

        self.tree[node] = max(self.tree[node * 2],self.tree[node * 2 + 1])

    def _apply(self, node, left, right, value):
        '''Lazy하도록 적용하는 함수'''
        self.haslazy[node] = True
        self.lazy[node] += value
        self.tree[node] += value


    def _push(self, node, left, right):
        '''하위 노드에 Lazy를 전달하는 함수'''
        if not self.haslazy[node]:
            return
        if left == right:
            return
        value = self.lazy[node]
        mid = (left + right) // 2
        self._apply(node * 2, left, mid, value)
        self._apply(node * 2 + 1, mid+1, right, value)
        self.lazy[node] = 0
        self.haslazy[node] = False

    def update(self, l, r, value):
        '''[l,r]구간에 모두 value를 더하는 함수'''
        self._update(1,0,self.N-1,l,r,value)

    def query(self, l, r):
        '''주어진 구간 중 가장 큰 수를 찾는 함수'''
        return self._query(1,0,self.N-1,l,r)


class IterativeLazySegmentTree:
    """
    비재귀 Lazy Segment Tree

    지원 연산:
        update(left, right, value):
            닫힌 구간 [left, right]의 모든 원소에 value를 더한다.

        query(left, right):
            닫힌 구간 [left, right]의 최댓값을 반환한다.

    시간 복잡도:
        생성: O(N)
        구간 갱신: O(log N)
        구간 쿼리: O(log N)
        공간 복잡도: O(N)

    기존 RecursivLazySegmentTree와 같은 인터페이스를 사용한다.
    재귀 호출과 매번 구간 경계를 전달하는 비용을 없애 Python에서 더 빠르게
    동작하도록 구현한 형태이다.

    내부 원리:
        1. 리프를 size번 인덱스부터 연속으로 배치한다.
        2. 갱신/조회 전에 양쪽 경계 경로의 lazy만 아래로 전달한다.
        3. 완전히 포함된 내부 구간에는 lazy 값을 남겨 둔다.
        4. 갱신 후 양쪽 경계에서 루트 방향으로 최댓값을 다시 계산한다.

    tree[node]에는 lazy[node]까지 반영된 구간 최댓값이 저장된다.
    자식의 최댓값에는 부모의 lazy가 포함되지 않으므로 부모를 다시 계산할
    때 max(left_child, right_child) + lazy[node]를 사용한다.
    """

    NEGATIVE_INFINITY = -10**30

    def __init__(self, arr):
        self.N = len(arr)
        if self.N == 0:
            raise ValueError("배열은 하나 이상의 원소를 가져야 합니다.")

        self.size = 1
        self.height = 0

        while self.size < self.N:
            self.size <<= 1
            self.height += 1

        # 리프가 아닌 노드에만 lazy 값이 필요하다.
        self.tree = [self.NEGATIVE_INFINITY] * (self.size << 1)
        self.lazy = [0] * self.size

        self.tree[self.size:self.size + self.N] = arr

        for node in range(self.size - 1, 0, -1):
            self.tree[node] = max(
                self.tree[node << 1],
                self.tree[node << 1 | 1],
            )

    def _apply(self, node, value):
        """node가 나타내는 구간 전체에 value를 적용한다."""
        self.tree[node] += value

        if node < self.size:
            self.lazy[node] += value

    def _push(self, node):
        """node에 쌓인 lazy 값을 두 자식에게 전달한다."""
        value = self.lazy[node]
        if value == 0:
            return

        self._apply(node << 1, value)
        self._apply(node << 1 | 1, value)
        self.lazy[node] = 0

    def _push_path(self, node):
        """루트부터 node까지 경로의 lazy 값을 위에서부터 전달한다."""
        for shift in range(self.height, 0, -1):
            self._push(node >> shift)

    def _pull_path(self, node):
        """node의 부모부터 루트까지 최댓값을 다시 계산한다."""
        while node > 1:
            node >>= 1
            self.tree[node] = (
                max(self.tree[node << 1], self.tree[node << 1 | 1])
                + self.lazy[node]
            )

    def _validate_range(self, left, right):
        if not 0 <= left <= right < self.N:
            raise IndexError(
                "구간은 0 <= left <= right < N을 만족해야 합니다."
            )

    def update(self, left, right, value):
        """닫힌 구간 [left, right]의 모든 원소에 value를 더한다."""
        self._validate_range(left, right)

        left += self.size
        right += self.size + 1  # 내부에서는 반열린 구간 [left, right)

        left_leaf = left
        right_leaf = right - 1

        self._push_path(left_leaf)
        self._push_path(right_leaf)

        while left < right:
            if left & 1:
                self._apply(left, value)
                left += 1

            if right & 1:
                right -= 1
                self._apply(right, value)

            left >>= 1
            right >>= 1

        self._pull_path(left_leaf)
        self._pull_path(right_leaf)

    def query(self, left, right):
        """닫힌 구간 [left, right]의 최댓값을 반환한다."""
        self._validate_range(left, right)

        left += self.size
        right += self.size + 1

        self._push_path(left)
        self._push_path(right - 1)

        result = self.NEGATIVE_INFINITY

        while left < right:
            if left & 1:
                result = max(result, self.tree[left])
                left += 1

            if right & 1:
                right -= 1
                result = max(result, self.tree[right])

            left >>= 1
            right >>= 1

        return result

