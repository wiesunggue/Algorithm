import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
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

        self.parent[u]=v
        if self.rank[u]==self.rank[v]:
            self.rank[v]+=1


N, Q = map(int,input().split())
disjointset = OptimizedDisjointSet(N)
trees = [0] * N
for i in range(N):
    x1,x2,y = map(int,input().split())
    trees[i] = x1,x2,y,i

trees.sort(key = lambda x:(x[0],-x[1]))

curMax = trees[0][1]
curMin = trees[0][0]
for i in range(1,N):
    x1,x2,y,s = trees[i]
    if curMax >= x1:
        curMax = max(curMax,x2)
        disjointset.merge(s,trees[i-1][3])
    else:
        curMin = x1
        curMax = x2

ans = []
for i in range(Q):
    a,b = map(int,input().split())
    a,b = disjointset.find(a-1),disjointset.find(b-1)
    ans.append(str(int(a==b)))

print("\n".join(ans))