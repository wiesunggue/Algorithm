# https://www.acmicpc.net/problem/20924
# 백준 20924번 트리의 기둥과 가지

# 입력이 20만줄이므로 빠른 입력이 필요하다 maxrecursion=1000이라서 20만으로 수정해야 함
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, R = map(int,input().split())
tree = [[]for i in range(N+1)]
visit = [0]*(N+1)
# 트리 만들기
for i in range(N-1):
    a,b,d = map(int,input().split())
    tree[a].append((b,d))
    tree[b].append((a,d))

tree[0].append((R,0)) # 부모 노드 문제 해결
tree[R].append((0,0))
pos = -1 # 기가 노드의 위치
def find_giga(node):
    '''기가 노드와 루트 노드로부터의 길이 구하기'''

    global pos
    if len(tree[node])>2:
        pos = node
        return 0
    for n,w in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            return find_giga(n)+w
    return 0

def find_length(node):
    '''트리의 길이 구하기'''
    #print(node)
    m = 0
    for n,w in tree[node]:
        if visit[n] ==0:
            visit[n] = 1
            m=max(m,find_length(n)+w)
    return m

# 루트 노드에서 시작
visit[R] = 1
Giga = find_giga(R) # 기가 노드를 찾는다
print(Giga, find_length(pos)) # 기가 노드로 부터 리프노드까지의 거리를 계산한다