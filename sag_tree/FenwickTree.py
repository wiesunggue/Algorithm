a = 6

# 가장 오른쪽 비트 반환하기
print(a&-a)

# 가장 오르쪽(최하위) 비트 제거하기
print(a&(a-1))

# 펜윅트리 FenwickTree
# 더하기에 대해 빠르게 계산하기
print("*"*50)
N = 10
tree = [0]*(N+1)

def segsum(tree, pos):
    pos += 1
    ret = 0
    while(pos>0):
        ret += tree[pos]
        pos &= (pos-1) # 구간을 가르키는 총 합 = 가장 오른쪽 비트를 지운다

    return ret

def segadd(tree,pos,val):
    pos += 1
    while(pos< len(tree)):
        tree[pos] += val
        pos += pos & - pos # 구간에 더해줘야 할 값을 가지는 인덱스 = 가장 오른쪽 비트에 1을 더해준다

for i in range(10):
    segadd(tree,i,i)

for i in range(10):
    print(segsum(tree,i))


def FenwickSum(tree,pos):
    ans = 0
    pos += 1
    while pos:
        ans += tree[pos]
        pos &= pos -1 # 최소 비트를 제거

    return ans

def FenwickAdd(tree,pos,val):
    pos += 1
    while pos:
        tree[pos] += val
        pos = (pos & -pos)

def f(a,k):
    if k==10:
        return
    for i in range(a):
        f(a,k)

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
