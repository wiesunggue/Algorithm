# https://www.acmicpc.net/problem/7469
# K번째 수
import math
class MergeSortTree:
    def __init__(self,N,arr):
        self.N = N
        self.size = 2 ** (math.ceil(math.log2(N))+1)
        self.arr = [[] for i in range(self.size)]
        self.initialize(0,self.N-1,1,arr)
    def initialize(self,left,right,node,arr):
        if left==right:
            self.arr[node] = [arr[left]]
            return self.arr[node]
        mid = (left+right)//2
        self.arr[node] = self.merge(self.initialize(left,mid,node*2,arr), self.initialize(mid+1,right,node*2+1,arr))
        return self.arr[node]

    def innerQuery(self,left,right,node,nodeleft,noderight):
        if noderight<left or right<nodeleft:
            return []
        if left<=nodeleft and noderight<=right:
            return self.arr[node]
        mid = (nodeleft+noderight)//2
        return self.merge(self.innerQuery(left,right,node*2,nodeleft,mid), self.innerQuery(left,right,node*2+1,mid+1,noderight))

    def query(self,left,right):
        return self.innerQuery(left,right,1,0,self.N-1)

    def merge(self,arr1,arr2):
        idx1,idx2 = 0,0
        arr = []
        while idx1<len(arr1) and idx2<len(arr2):
            if arr1[idx1]<arr2[idx2]:
                arr.append(arr1[idx1])
                idx1 += 1
            else:
                arr.append(arr2[idx2])
                idx2 += 1

        arr.extend(arr1[idx1:])
        arr.extend(arr2[idx2:])

        return arr

N,Q = map(int,input().split())
arr = list(map(int,input().split()))
mst = MergeSortTree(N,arr)

ans = []
for q in range(Q):
    i,j,k = map(int,input().split())
    #print(mst.query(i-1,j-1))
    ans.append(str(mst.query(i-1,j-1)[k-1]))

print('\n'.join(ans))