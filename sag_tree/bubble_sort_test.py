# https://www.acmicpc.net/problem/1517
# 버블 소트 펜윅트리연습

class FenwickTree:
    def __init__(self,N):
        self.N = N
        self.arr = [0]*(N+1)

    def Add(self,pos,value):
        pos += 1
        while pos<self.N:
            self.arr[pos] += value
            pos += pos & -pos

    def onewaySum(self,pos):
        pos += 1
        ret = 0
        while pos:
            ret += self.arr[pos]
            pos &= pos-1

        return ret

MAX_LEN = 500001
N = int(input())
fw = FenwickTree(MAX_LEN)
arr = list(map(int,input().split()))
compressedarr = []
for i in range(N):
    compressedarr.append((arr[i],i))
compressedarr.sort()
ans = 0
for i in range(N):
    ans += fw.onewaySum(MAX_LEN)-fw.onewaySum(compressedarr[i][1])
    fw.Add(compressedarr[i][1],1)

print(ans)