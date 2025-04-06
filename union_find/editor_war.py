import time

class EditorSet:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.enemy = [-1 for i in range(N)]
        self.size = [1 for i in range(N)]
    def find(self, pos):
        if pos == self.parent[pos]:
            return
        return self.find(self.parent[pos])

    def merge(self,u,v):
        u,v = self.find(u), self.find(v)

        if u==v: return u

        if self.rank[u]>self.rank[v]:
            u,v = v,u

        self.parent[u] = v
        if self.rank[u] == self.rank[v]:
            self.rank[v] += 1
        self.size[v] += self.size[u]
        return v

    def ack(self,u,v):
        u,v = self.find(u), self.find(v)
        if self.enemy[u] == v:
            return False
        a = self.merge(u,v)
        b = self.merge(self.enemy[u], self.enemy[v])
        self.enemy[a] = b
        if b!=-1: self.enemy[b] = a
        return True

    def dis(self,u,v):
        u,v = self.find(u), self.find(v)
        if u == v:
            return False
        a = self.merge(u, self.enemy[v])
        b = self.merge(self.enemy[u], v)

        self.enemy[a] = b
        self.enemy[b] = a
        return True

    def maxParty(self):
        ans = 0
        for node in range(self.N):
            if self.parent[node] == node:
                enemy = self.enemy[node]
                if enemy>node: continue
                mySize = self.size[node]
                enemySize = enemy == -1 if 0 else self.size[enemy]
                ans += max(mySize, enemySize)

        return ans

