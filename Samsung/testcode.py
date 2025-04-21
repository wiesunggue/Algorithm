import sys
input = sys.stdin.readline

class SegmentTree():
    def __init__(self,N):
        self.MAX_VALUE = 10**10
        self.N = N
        self.arr = [0] * (4*N)

    def initialize(self,left,right,node,initarray):
        if left==right:
            self.arr[node] = initarray[left]
            return self.arr[node]
        mid = (left+right)//2
        self.arr[node] = min(self.initialize(left,mid,node*2,initarray) , self.initialize(mid+1,right,node*2+1,initarray))
        return self.arr[node]

    def innerquery(self,left,right,node,nodeleft,noderight):
        if right<nodeleft or noderight<left:
            return self.MAX_VALUE
        if left<=nodeleft and noderight<=right:
            return self.arr[node]
        mid = (nodeleft+noderight)//2
        return min(self.innerquery(left,right,node*2,nodeleft,mid),self.innerquery(left,right,node*2+1,mid+1,noderight))

    def innerupdate(self,index,newvalue,node,nodeleft,noderight):
        if index<nodeleft or noderight<index:
            return self.arr[node]
        if nodeleft==noderight:
            self.arr[node]=newvalue
            return self.arr[node]

        mid = (nodeleft+noderight)//2
        self.arr[node] = min(self.innerupdate(index,newvalue,node*2,nodeleft,mid),self.innerupdate(index,newvalue,node*2+1,mid+1,noderight))
        return self.arr[node]

    def update(self,index,value):
        return self.innerupdate(index,value,1,0,self.N-1)
    def query(self,left,right):
        return self.innerquery(left,right,1,0,self.N-1)
N = int(input())
segtree = SegmentTree(N)
initarray = list(map(int,input().split()))
segtree.initialize(0,N-1,1,initarray)
for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a==1:
        segtree.update(b-1,c)
    else:
        if b>c:
            b,c = c,b
        print(segtree.query(b-1,c-1))