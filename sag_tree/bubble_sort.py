import sys
rinput = sys.stdin.readline
rprint = sys.stdout.write
INT_MAX=10**9
class Segment_Tree():
    def __init__(self,N):
        self.array = [0]*4*N
        self.N = N

    def get_left(self,node):
        return 2*node
    def get_right(self,node):
        return 2*node+1
    def get_parent(self,node):
        return node//2

    def make_tree(self,arr,left,right,node):
        if left==right:
            self.array[node]=arr[left]
            return self.array[node]

        mid = (left+right)//2
        left_tree=self.make_tree(arr,left,mid,self.get_left(node))
        right_tree=self.make_tree(arr,mid+1,right,self.get_right(node))

        self.array[node]=left_tree+right_tree

        return self.array[node]

    def inner_query(self,left,right,node,nodeleft,noderight):
        if right<nodeleft or noderight<left:
            return 0

        if left<=nodeleft and noderight <=right:
            return self.array[node]

        mid = (nodeleft+noderight)//2
        return self.inner_query(left,right,node*2,nodeleft,mid)+self.inner_query(left,right,node*2+1,mid+1,noderight)

    def query(self,left, right):
        return self.inner_query(left,right,1,0,self.N-1)

    def inner_update(self,index,newValue,node, nodeleft, noderight):
        if index < nodeleft or noderight <index:
            return self.array[node]

        if nodeleft==noderight:
            self.array[node]=newValue
            return self.array[node]

        mid = (nodeleft+noderight)//2
        self.array[node]=self.inner_update(index, newValue,node*2,nodeleft,mid)+self.inner_update(index,newValue,node*2+1,mid+1,noderight)
        return self.array[node]
    def update(self,index, newValue):
        return self.inner_update(index, newValue, 1, 0, self.N-1)

def solve():
    N = int(input())
    arr = list(map(int,input().split()))
    s = list(set(arr))
    s.sort()
    arr_dict = {}
    for i in range(len(s)):
        arr_dict[s[i]]=i
    node=500100
    Segsum = Segment_Tree(node)
    ans=0
    for i in arr:
        temp = arr_dict[i]
        ans+=Segsum.query(temp+1,node)
        Segsum.update(temp,Segsum.query(temp,temp)+1)
    print(ans)
if __name__ =='__main__':
    solve()