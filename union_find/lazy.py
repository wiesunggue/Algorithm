# https://www.acmicpc.net/problem/24391
# 백준 24391번 귀찮은 해강이
class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0]*size
        self.N = size

    def find(self,u):
        if self.parent[u] == u:
            return u
        return self.find(self.parent[u])

    def merge(self,u,v):
        u,v = self.find(u),self.find(v)
        if u==v:
            return
        if self.rank[u]>self.rank[v]:
            u,v = v,u

        self.parent[u] = v
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1


N,M = map(int,input().split())
disjointset = OptimizedDisjointSet(N+1)

for i in range(M):
    a,b = map(int,input().split())
    disjointset.merge(a,b)

arr = list(map(int,input().split()))
before = disjointset.find(arr[0])
ans = 0
for i in range(N):
    b = disjointset.find(arr[i])
    print(b)
    if before != b:
        before = b
        ans += 1
print(ans)