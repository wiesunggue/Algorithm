# https://www.acmicpc.net/problem/2268
# 수들의 합 7
import sys
input = sys.stdin.readline

class FenwickTree():
    def __init__(self,N):
        self.N = N
        self.arr = [0] * (N+1)

    def segadd(self,pos,value):
        pos += 1
        while pos<self.N:
            self.arr[pos] += value
            pos += (pos & -pos)

    def segsum(self,pos):
        ret = 0
        pos += 1
        while pos>0:
            ret += self.arr[pos]
            pos &= (pos-1)

        return ret
    def twoWaySum(self, start, end):
        return self.segsum(end) - self.segsum(start)
    def writeValue(self):
        print(self.arr)
N, M =map(int,input().split())
fw = FenwickTree(12)


fw.segadd(1,1)
fw.segadd(2,10)
fw.segadd(3,100)
fw.segadd(4,1000)
fw.segadd(5,10000)
fw.segadd(6,100000)
fw.segadd(7,1000000)
fw.segadd(8,10000000)
fw.segadd(9,100000000)
fw.segadd(10,1000000000)
print(fw.segsum(1))
print(fw.segsum(2))
print(fw.segsum(3))
print(fw.segsum(4))
print(fw.segsum(5))
print(fw.twoWaySum(1,5)) # 2번부터 5번까지 합