# 이론 연습
class FenwickTree:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (self.N + 1)

    def oneWaySum(self, pos):
        ans = 0
        while pos:
            ans += self.tree[pos]
            pos &= pos - 1

        return ans

    def twoWaySum(self, start, end):
        return self.oneWaySum(end) - self.oneWaySum(start)

    def add(self, pos, value):
        pos += 1
        while pos<self.N:
            self.tree[pos] += value
            pos += pos & -pos

class FenwickTree2:
    def __init__(self,N):
        self.N = N
        self.tree = [0] * (N+1)

    def add(self, pos, value):
        pos += 1
        while pos:
            self.tree[pos] += value
            pos = pos & -pos


    def onewaySum(self, pos):
        ans = 0
        while pos:
            ans += self.tree[pos]
            pos &= pos-1

        return ans

    def twowaySum(self,start, end):
        return self.onewaySum(end)-self.onewaySum(start)

N = 1000
FW = FenwickTree(N)
FW.add(0,1)
FW.add(1,10)
FW.add(2,100)
FW.add(3,1000)
FW.add(4,10000)
FW.add(5,100000)

print(FW.twoWaySum(0,5))
