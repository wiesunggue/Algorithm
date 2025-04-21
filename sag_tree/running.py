# https://www.acmicpc.net/problem/2517
# 달리기
import random
import time

import sys
input= sys.stdin.readline

class FenwickTree:
    def __init__(self,N):
        self.N = N+1
        self.arr = [0]*self.N

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

N = int(input())
arr = [int(input())+10 for i in range(N)]
s=  time.time()
#N = 500000
#arr = [random.randint(1,N) for i in range(N)]
arr2=sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
e = time.time()
print(e-s)
fw = FenwickTree(N+1)
ans = []
for i in range(N):
    t = dic[arr[i]]
    ans.append(str(i - fw.onewaySum(dic[arr[i]] - 1) + 1))
    fw.Add(dic[arr[i]], 1)
ee = time.time()
print(ee-e)
#print('\n'.join(ans))
