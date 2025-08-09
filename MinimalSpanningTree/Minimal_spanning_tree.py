# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리

# 크루스칼 방식
class UnionFind:
    def __init__(self,N):
        self.N = N
        self.Parent = [i for i in range(N)]
        self.Rank = [1 for i in range(N)]
