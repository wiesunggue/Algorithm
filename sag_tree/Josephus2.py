# https://www.acmicpc.net/problem/1168
# 백준 요세푸스 2 문제

class FenwickTree:
    def __init__(self,N):
        self.N = N+1
        self.tree = [0] * self.N
        self.total = 0

    def segAdd(self,pos,v):
        pos +=1
        while pos<self.N:
            self.tree[pos] += v
            pos += pos & -pos
        self.total += v

    def segSum(self,pos):
        if pos < 0:
            return 0
        pos += 1
        ret = 0
        while pos:
            ret += self.tree[pos]
            pos &= pos-1

        return ret

    def search(self,now,k):
        """이분탐색으로 k의 position을 찾는 함수"""
        k = k % self.total
        if k==0:
            k += self.total
        nowCount = self.segSum(now)
        if self.total - nowCount >= k: # k가 뒤에 있는 경우
            start = now
            end = self.N - 1
        else: # k가 앞에 있는 경우
            k = k - self.total + nowCount # 뒤에 있는 수 만큼 k감소
            start = 0
            end = now

        ans = self.leftBinarySearch(start,end,k)
        self.segAdd(ans,-1) # 값 삭제

        return ans

    def leftBinarySearch(self,start,end,target):
        startPos = start - 1
        startCount = self.segSum(startPos)
        while start<=end:
            print(start,end,target)
            mid = (start+end)//2
            ret = self.segSum(mid)-startCount
            if target == ret:
                result = mid
                end = mid - 1
            elif target > ret:
                start = mid + 1
            else:
                end = mid - 1

        return result

N,K = map(int,input().split())

fw = FenwickTree(N)
for i in range(N):
    fw.segAdd(i,1)

idx = -1
ans = []
for i in range(N):
    idx = fw.search(idx,K)
    ans.append(str(idx+1))

print('<'+', '.join(ans)+'>')