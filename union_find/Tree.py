# https://www.acmicpc.net/problem/13244
# 백준 13244번 Tree 문제
class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.N = size

    def find(self,u):
        if u== self.parent[u]:
            return u
        return self.find(self.parent[u])

    def merge(self,u,v):
        u,v = self.find(u), self.find(v)
        if u==v:
            return
        if self.rank[u]>self.rank[v]:
            u,v = v,u
        self.parent[u] = v
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
def solutions():
    N = int(input())
    M = int(input())
    disjointset = OptimizedDisjointSet(N+1)
    ans = True
    for i in range(M):
        u,v = map(int,input().split())
        if disjointset.find(u)!=disjointset.find(v):
            disjointset.merge(u,v)
        else:
            ans=False
    root = disjointset.find(1)
    for i in range(1,N+1):
        ans *= root==disjointset.find(i)
    print('tree' if ans== True else 'graph')

if __name__ =='__main__':
    T = int(input())
    for test in range(T):
        solutions()