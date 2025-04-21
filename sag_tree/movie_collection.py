# https://www.acmicpc.net/problem/3653
# 영화 수집

# 아이디어 
# 1. 영화 idx 접근 배열 생성
# 2. 영화 볼 때마다 마지막 노드에 영화 추가

import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self,N,arr):
        self.N = N
        self.arr = [0] * (self.N * 4)
        self.initialize(0,self.N-1,1,arr)

    def initialize(self,left,right,node,initarray):
        if left==right:
            self.arr[node] = initarray[left]
            return self.arr[node]
        mid = (left+right)//2
        self.arr[node] = self.initialize(left,mid,node*2,initarray) + self.initialize(mid+1,right,node*2+1,initarray)
        return self.arr[node]

    def innerquery(self,left,right,node,nodeleft,noderight):
        if noderight<left or right<nodeleft:
            return 0
        if left<=nodeleft and noderight<=right:
            return self.arr[node]
        mid = (nodeleft+noderight)//2
        return self.innerquery(left,right,node*2,nodeleft,mid)+self.innerquery(left,right,node*2+1,mid+1,noderight)

    def innerupdate(self,index,value,node,nodeleft,noderight):
        if noderight<index or index<nodeleft:
            return self.arr[node]

        if nodeleft==noderight:
            self.arr[node] = value
            return self.arr[node]

        mid = (nodeleft+noderight)//2
        self.arr[node] = self.innerupdate(index,value,node*2,nodeleft,mid)+self.innerupdate(index,value,node*2+1,mid+1,noderight)
        return self.arr[node]

    def query(self,left,right):
        return self.innerquery(left,right,1,0,self.N-1)

    def update(self,index,value):
        return self.innerupdate(index,value,1,0,self.N-1)

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    arr = [1 for i in range(N)]+[0 for i in range(M)]
    size = len(arr)
    movies = list(map(int,input().split()))
    idx = N
    visit = [N-i-1 for i in range(N)]
    tree = SegmentTree(size,arr)
    ans = []
    for m in range(M):
        movie = movies[m] - 1
        ans.append(str(tree.query(visit[movie]+1,size)))
        tree.update(visit[movie],0)
        visit[movie] = idx
        idx += 1
        tree.update(visit[movie],1)
    print(' '.join(ans))