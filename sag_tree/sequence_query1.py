# https://www.acmicpc.net/problem/13537
# 수열과 쿼리1

import sys,bisect
input = sys.stdin.readline

class MergeSortTree:
    def __init__(self,N,arr):
        self.N = N
        self.arr = [[] for i in range(4*N)]
        self.initialize(0,self.N-1,1,arr)
    def initialize(self,left,right,node,initarray):
        if left==right:
            self.arr[node] = [initarray[left]]
            return self.arr[node]
        mid = (left+right)//2
        self.arr[node] = self.merge(self.initialize(left,mid,node*2,initarray), self.initialize(mid+1,right,node*2+1,initarray))
        return self.arr[node]

    def innerquery(self,left,right,node,nodeleft,noderight):
        if noderight<left or right<nodeleft:
            return 0
        if left<=nodeleft and noderight<=right:
            print(self.arr[node],k)
            return len(self.arr[node]) - bisect.bisect_right(self.arr[node],k)
        mid = (nodeleft+noderight)//2
        return self.innerquery(left,right,node*2,nodeleft,mid) + self.innerquery(left,right,node*2+1,mid+1,noderight)

    def query(self,left,right,k):
        return self.innerquery(left,right,1,0,self.N-1)

    def merge(self,arr1,arr2):
        ret = []
        idx1,idx2 = 0,0
        while idx1<len(arr1) and idx2<len(arr2):
            if arr1[idx1]<arr2[idx2]:
                ret.append(arr1[idx1])
                idx1 += 1
            else:
                ret.append(arr2[idx2])
                idx2 += 1
        ret.extend(arr1[idx1:])
        ret.extend(arr2[idx2:])
        return ret

N = int(input())
arr = list(map(int,input().split()))
tree = MergeSortTree(N,arr)
ans = []
M = int(input())

for i in range(M):
    i,j,k = map(int,input().split())
    ans.append(str(tree.query(i-1,j-1,k)))

print('\n'.join(ans))