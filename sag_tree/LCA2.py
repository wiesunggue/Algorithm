# https://www.acmicpc.net/problem/11438
# 백준 LCA문제

# 기본 이론으로는 트리 전위 순회 시 만들어지는 방문 목록을 구성하면
# 정점 u, v사이에서 LCA는 항상 방문 목록에서 u, v 사이에서 깊이가 최소인 위치이다.

# 필요한것
# 상위 노드는 작은 index를 가지도록 트리 재조정
# 가장 먼저 등장하는 노드의 위치를 저장하는 배열(전위 순회 순) -> 이렇게 되면 최소인 위치 = 최소인 노드가 된다
# 노드별 깊이를 저장
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
MAX_LEN = 100010


trip = []
no2serial = [0] * MAX_LEN
serial2no = [0] *  MAX_LEN
depth = [0] * MAX_LEN
locInTrip = [0] * MAX_LEN
nextSerial = 0
def traverse(here,d):
    """bfs로 순회하면서 인덱스를 설정하고 깊이를 저장하는 함수"""
    if visited[here]==1:
        return
    visited[here] = 1
    global nextSerial
    no2serial[here] = nextSerial
    serial2no[nextSerial] = here
    nextSerial += 1

    depth[here] = d
    locInTrip[here] = len(trip) # 가장 먼저 나오는 위치 저장
    trip.append(no2serial[here])

    for there in graph[here]:
        traverse(there,d+1)
        trip.append(no2serial[here])

class RMQ:
    def __init__(self):
        root = 1
        traverse(root,0)
        self.N = len(trip)
        self.arr = [0] * (4*self.N) # 가장 가까운 2N이 더 좋다
        self.MAX_VALUE = 10**10

        self.initialize(trip,0,self.N-1,1)

    def initialize(self,arr,left,right,node):
        if left==right:
            self.arr[node] = arr[left]
            return self.arr[node]

        mid = (left+right)//2
        self.arr[node] = min(self.initialize(arr,left,mid,node*2), self.initialize(arr,mid+1,right,node*2+1))
        return self.arr[node]

    def innerUpdate(self,index,value,node,nodeleft,noderight):
        if index<left or index<nodeleft:
            return 0

        if nodeleft==noderight:
            self.arr[node] = value
            return self.arr[node]
        mid = (nodeleft+noderight)//2
        self.arr[node] = min(self.innerUpdate(left,right,node*2,nodeleft,mid), self.innerUpdate(left,right,node*2+1,mid+1,noderight))
        return self.arr[node]

    def innerQuery(self,left,right,node,nodeleft,noderight):
        if noderight<left or right<nodeleft:
            return self.MAX_VALUE
        if left <= nodeleft and noderight <= right:
            return self.arr[node]

        mid = (nodeleft+noderight)//2
        return min(self.innerQuery(left,right,node*2,nodeleft,mid),self.innerQuery(left,right,node*2+1,mid+1,noderight))

    def Update(self,index,value):
        return self.innerUpdate(index,value,1,0,self.N-1)

    def Query(self,left,right):
        return self.innerQuery(left,right,1,0,self.N-1)

    def distance(self,u,v):
        lu,lv = locInTrip[u],locInTrip[v]
        if lu>lv:
            lu,lv = lv,lu
        lca = serial2no[self.Query(lu,lv)]
        return depth[u]+depth[v]-depth[lca]*2

    def LCA(self,u,v):
        lu,lv = locInTrip[u],locInTrip[v]
        if lu>lv:
            lu,lv = lv,lu
        lca = serial2no[self.Query(lu,lv)]
        return lca

N = int(input())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

rmq = RMQ()
M = int(input())
ans = []
for i in range(M):
    u,v = map(int,input().split())
    ans.append(str(rmq.LCA(u,v)))

print('\n'.join(ans))