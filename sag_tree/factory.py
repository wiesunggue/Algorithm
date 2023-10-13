# https://www.acmicpc.net/problem/7578
# 공장 문제 -> 세그먼트트리 기본 문제로 버블 소트와 같은 문제다.

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

n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

d1 = {}
d={}
for i in range(n):
    d1[arr2[i]]=i
for i in range(n):
    d[i]=d1[arr1[i]]

tree=[0]*2*n
ans=0
for i in range(n):
    ans+=query(d[i]+1,n)
    update(d[i],1)
print(ans)