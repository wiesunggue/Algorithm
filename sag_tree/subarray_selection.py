import sys
input = sys.stdin.readline
n=1

def update(index, value):
    index += N
    tree[index] = value

    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] + tree[index * 2 + 1]


def query(left, right):
    result = 0
    left += N
    right += N

    while left < right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        left //= 2

        if right % 2 == 1:
            right -= 1
            result += tree[right]
        right //= 2
    return result

N = int(input())
tree=[[0,10**9]for i in range(N)]
arr = list(map(int,input().split()))