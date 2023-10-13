import heapq
import sys
input = sys.stdin.readline
def dijs():
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    node = [[]for i in range(n+1)]
    table = [10**10]*(n+1)
    visit = [0]*(n+1)
    check = [0]*(n+1)
    for i in range(m):
        a,b,c = map(int,input().split())
        if (a==h and b==g) or (a==g and b==h):
            c-=0.1
        node[a].append((b,c))
        node[b].append((a,c))
    goal = [int(input())for i in range(t)]
    table[s]=0
#    visit[s]=1
    pq = []
    heapq.heappush(pq,(table[s],s))
    while pq:
        weight,idx=heapq.heappop(pq)
        if visit[idx]!=0:
            continue
        visit[idx]=1
        for i,w in node[idx]:
            if weight+w<=table[i]:
                table[i]=weight+w
                check[i]=check[idx] | (idx==g and i==h) | (idx==h and i==g) | (weight+w==table[i] and check[i])
                heapq.heappush(pq,(table[i],i))
    print(table)
    for i in sorted(goal):
        if type(table[i])!=int:
            print(i,end=' ')
    print()

for i in range(int(input())):
    dijs()