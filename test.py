from math import log2
import sys
rinput = sys.stdin.readline
rprint = sys.stdout.write
MAX_VALUE = 1000000007
class Segment_Tree():
    def __init__(self,N):
        arr_size=2**(int(log2(N))+2)
        self.array = [0]*arr_size
        self.N = N

    def make_tree(self,arr,left,right,node):
        if left==right:
            self.array[node]=arr[left]
            return self.array[node]%MAX_VALUE
        mid = (left+right)//2
        self.array[node]=(self.make_tree(arr,left,mid,node*2)*self.make_tree(arr,mid+1,right,node*2+1))%MAX_VALUE

        return self.array[node]

    def in_query(self,left,right,node,nodeleft,noderight):
        if noderight<left or right<nodeleft:
            return 1

        if left<=nodeleft and noderight<=right:
            return self.array[node]%MAX_VALUE

        mid = (nodeleft+noderight)//2
        return (self.in_query(left,right,node*2,nodeleft,mid)*self.in_query(left,right,node*2+1,mid+1,noderight))%MAX_VALUE

    def query(self,left,right):
        return self.in_query(left,right,1,0,self.N-1)%MAX_VALUE

    def in_update(self,index,newvalue,node,nodeleft,noderight):
        if index<nodeleft or noderight<index:
            return self.array[node]%MAX_VALUE

        if nodeleft==noderight:
            self.array[node]=newvalue%MAX_VALUE
            return self.array[node]
        mid = (nodeleft+noderight)//2
        self.array[node]=(self.in_update(index,newvalue,node*2,nodeleft,mid)*self.in_update(index,newvalue,node*2+1,mid+1,noderight))%MAX_VALUE

        return self.array[node]%MAX_VALUE

    def update(self,index,newvalue):
        return self.in_update(index,newvalue,1,0,self.N-1)%MAX_VALUE

class NaiveDisjointSet():
    def __init__(self,size):
        self.parent=[i for i in range(size)]
        self.N = size

    def find(self,u):
        if u==self.parent[u]:
            return u
        return self.find(self.parent[u])

    def merge(self, u, v):
        u,v = self.find(u),self.find(v)
        if u==v:
            return
        self.parent[u]=v
class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.arr = [1 for i in range(size)]
        self.N = size

    def find(self,u):
        if u==self.parent[u]:
            return u
        return self.find(self.parent[u])

    def merge(self,u,v):
        u,v = self.find(u),self.find(v)
        if u==v:
            return
        if self.rank[u]>self.rank[v]:
            u,v = v,u

        self.arr[self.find(v)]=self.arr[self.find(u)]+self.arr[self.find(v)]
        self.parent[u]=v
        if self.rank[u]==self.rank[v]:
            self.rank[v]+=1

    def size(self,u):
        return self.arr[self.find(u)]
def solve():
    a,b,c = map(int,input().split())
    arr = [int(rinput()) for _ in range(a)]
    seg_tree = Segment_Tree(a)
    seg_tree.make_tree(arr,0,a-1,1)
    query_arr = [list(map(int,rinput().split())) for _ in range(b+c)]
    for ii in query_arr:
        if ii[0]==1:
            seg_tree.update(ii[1]-1,ii[2])
        else:
            rprint("{}\n".format(seg_tree.query(ii[1]-1,ii[2]-1)))


if __name__ == '__main__':
    solve()