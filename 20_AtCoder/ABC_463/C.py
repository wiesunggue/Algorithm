import sys
input = sys.stdin.readline


class IterativeSegmentTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = arr
        self.size = 1

        while self.size < self.N:
            self.size *= 2

        self.tree = [[0,0] for i in range((2 * self.size))]

        for i in range(self.N):
            self.tree[self.size + i] = arr[i]

        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def query(self, left, right):
        left += self.size
        right += self.size

        result = [-1,0]

        while left <= right:
            if left % 2 == 1:
                result = max(result,self.tree[left])
                left += 1

            if right % 2 == 0:
                result = max(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result

N = int(input())
takahashi = [list(map(int,input().split())) for i in range(N)]
takahashi.sort(key=lambda x:x[1])

tree = IterativeSegmentTree(takahashi)
Q = int(input())
T = list(map(int,input().split()))
sortedT = []
for i in range(Q):
    sortedT.append((T[i],i))

sortedT.sort()
ans = [0] * Q

# H에 대해 정렬된 상태
# L을 기준으로 제거해야 함
# 혹은 L을 기준으로 정렬하고, H에 대해 최댓값을 찾아야 함

l = 0
before_l = -1
for i in range(Q):
    while l<N:
        if takahashi[l][1] <= sortedT[i][0]:
            l += 1
        else:
            break
    if before_l == l:
        ans[sortedT[i][1]] = ans[sortedT[i-1][1]]
    else:
        ans[sortedT[i][1]] = str(tree.query(l,N-1)[0])
    before_l = l

print('\n'.join(ans))