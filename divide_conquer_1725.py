# 분할정복
# https://www.acmicpc.net/problem/1725 히스토그램
# 가장 큰 직사각형을 구하는 문제

import sys
input=sys.stdin.readline
N=int(input())
arr=[int(input()) for i in range(N)]

def solve(left,right):
    if left==right:
        return arr[left]
    mid=(left+right)//2
    ret=max(solve(left,mid),solve(mid+1,right),min(arr[mid],arr[mid+1])*2)
    l,h=mid,mid+1
    height=min(arr[l],arr[h])
    while (left<l or h<right):
        if h<right and (arr[l-1]<arr[h+1] or l==left):
            h+=1
            height=min(height,arr[h])
        else:
            l-=1
            height=min(height,arr[l])
        ret=max(ret,height*(h-l+1))
            
    return ret

print(solve(0,N-1))