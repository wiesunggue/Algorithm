# https://www.acmicpc.net/problem/1939
# 중량 제한 문제
# 분리 집합 문제

# 최적화된 유니온 파인드
class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        self.weight = [10**12 for i in range(size)]
        self.N = size

    def find(self,u):
        self.cnt+=1
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
N,M = map(int,input().split())
node = OptimizedDisjointSet(N+1)
for i in range(M):
    a,b,c = map(int,input().split())