# https://www.acmicpc.net/problem/20666
# 인물이와 정수
import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
arr=list(map(int,input().split()))
visit =[0]*N
P = int(input())
tips = {i:[] for i in range(N)}
for i in range(P):
    a,b,t=map(int,input().split())
    arr[b-1]+=t
    tips[a-1].append((b-1,t))
    
# 힙 구성하기
pq = []
for i in range(N):
    heapq.heappush(pq,(arr[i],i))

m=0
ans=0
while m<M:
    print(pq)
    difficulty,nextSerial = heapq.heappop(pq)
    if visit[nextSerial]!=0:
        continue
    visit[nextSerial]=1
    m+=1
    ans=max(difficulty,ans)
    for i,diff in tips[nextSerial]:
        if visit[i]==0:
            arr[i]-=diff
            heapq.heappush(pq,(arr[i],i))
        
print(tips)
print(arr)
print(ans)