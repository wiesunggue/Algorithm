from collections import deque
N=int(input())
arr=list(map(int,input().split()))
arr.sort()
l={}
def recur(n,i,v):
    if n>N:
        return
    l[v]=1
    for k in range(i+1,N):
        recur(n+1,k,v+arr[k])

recur(0,-1,0)

for i in range(1,10000000):
    if l.get(i)!=1:
        print(i)
        break
        