import time

class NavieDisjointSet:
    def __init__(self,N):
        self.N = N
        self.parent = [i for i in range(N)]

    def find(self,u):
        if u == self.parent[u]:
            return u
        return self.find(self.parent[u])

    def merge(self,u,v):
        u,v = self.find(u),self.find(v)
        if u==v:
            return
        self.parent[u] = v

class OptimizedDisjointSet:
    def __init__(self,N):
        self.N = N
        self.Parent = [i for i in range(N)]
        self.Rank = [1 for i in range(N)]

    def find(self,u):
        if self.Parent[u] == u:
            return u
        return self.find(self.Parent[u])

    def merge(self,u,v):
        u,v = self.find(u), self.find(v)
        if u==v:
            return
        if self.Rank[u] > self.Rank[v]:
            u,v = v,u # rank는 항상 v가 큼

        self.Parent[u] = v
        if self.Rank[u] == self.Rank[v]:
            self.Rank[v] += 1 # 같다면 v->u로 연결했으므로 v의 rank를 1 추가