import sys
input = sys.stdin.readline
def update(index, value):
    index += n
    tree[index] = value

    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] + tree[index * 2 + 1]


def query(left, right):
    result = 0
    left += n
    right += n

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

def binary(rank):
    start=0
    end = n
    for i in range(100):
        mid = (start+end)//2
        if query(0,mid+1)>=rank: # 0~mid까지 사탕의 개수
            end=mid
        else:
            start=mid+1
    return start

n=1000001
tree = [0]*3*n
for i in range(int(input())):
    arr=list(map(int,input().split()))
    if arr[0]==1:
        idx=binary(arr[1])
        print(idx)
        update(idx,query(idx,idx+1)-1)
    else:
        update(arr[1],query(arr[1],arr[1]+1)+arr[2])