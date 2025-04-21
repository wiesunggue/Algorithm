# https://www.acmicpc.net/problem/1168
# 요세푸스 2 문제


class FenwickTree():
    def __init__(self,N):
        self.N = N
        self.arr = [0] * (N+1)
        self.total = N

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
        if start<=end:
            return self.segsum(end) - self.segsum(start-1)
        else:
            return self.twoWaySum(start,self.N) - self.twoWaySum(0,end)

    def binarysearch(self,k):
        offset = self.before
        start = offset
        end = offset - 1

        k = k%self.total
        while start+1<end:
            mid = (start+end-2*offset)//2 + offset
            if self.segsum(mid) > k:
                end = mid - 1
            else:
                start = mid + 1
        print(mid,self.segsum(mid))
        self.segadd(mid,-1)
        self.total -= 1
        self.before = mid
        return mid


N,K = map(int,input().split())
fw = FenwickTree(N)
for i in range(N):
    fw.segadd(i,1)

for i in range(N):
    print(fw.binarysearch(K))