# 유니온 파인드
# 개념 : 집합을 합치기 a와 b가 같은 집합이고 b와 c가 같은 집합이면 a b c모두 같은 집합이 된다
# 응용 예제 : 집합 연산하기, 사이클 검사하기

# 유니온 파인드 클래스 정의하기
# 유니온 파인드 기본
import random
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

# 최적화된 유니온 파인드
class OptimizedDisjointSet():
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
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
