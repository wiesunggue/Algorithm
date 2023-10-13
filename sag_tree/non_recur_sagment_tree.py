import sys
from math import log2
input = sys.stdin.readline
n=0
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


N = int(input())
arr = list(map(int,input().split()))
#    arr = [random.randint(1,10**9)for i in range(N)]
tree = [0]*2*N
s = list(set(arr))
s.sort()
arr_dict = {}
n=len(s)+1
for i in range(len(s)):
    arr_dict[s[i]]=i

ans=0
for i in arr:
    temp = arr_dict[i]
    ans += query(temp + 1, len(s) + 1)
    update(temp,query(temp,temp+1)+1)
print(ans)