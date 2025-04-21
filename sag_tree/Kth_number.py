# https://www.acmicpc.net/problem/7469
# K번째 수
import math
class MergeSortTree:
    def __init__(self,N):
        self.N = N
        self.size = 2 ** math.ceil(math.log2(N))
        self.arr = [0]*self.size

    def initialize(self,left,right,node,arr):
        if left==right:
            self.arr[node] = arr[left]
        mid = (left+right)//2
        self.arr[node] = self.initialize(left,mid,node*2,arr)+self.initialize(mid+1,right,node*2+1,arr)
        return self.arr[node]