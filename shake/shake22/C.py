import sys
input = sys.stdin.readline

N = int(input())
m1,m2,m3 =map(int,input().split())

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

day1=OptimizedDisjointSet(N+1)
day2=OptimizedDisjointSet(N+1)
day3=OptimizedDisjointSet(N+1)

for i in range(m1):
    a,b = map(int,input().split())
    day1.merge(a,b)
for i in range(m2):
    a, b = map(int, input().split())
    day2.merge(a,b)
for i in range(m3):
    a, b = map(int, input().split())
    day3.merge(a,b)

d={}
for i in range(1,N+1):
    a,b,c=day1.find(i),day2.find(i),day3.find(i)
    if d.get(str((a,b,c)))==None:
        d[str((a,b,c))]=[]
    d[str((a,b,c))].append(i)

print(d.values())
A=d.values()
B=[]
cnt=0
for i in A:
    if len(i)!=1:
        cnt+=1
        B.append(i)

print(cnt)
for i in B:
    print(*i)
