# https://www.acmicpc.net/problem/19542
# 백준 19542번 전단지 돌리기

# 문제 해결 전략
# 사이클이 없는 그래프 문제
# dfs를 두번 사용해서 정답 찾기
# 1. 끝점 만날 때 부터 시작해서 1씩 증가
# 2. 끝점이 D보다 큰 경우에만 방문하도록 해서 dfs 탐색
import sys
sys.setrecursionlimit(10**5+1)
input = sys.stdin.readline

def dfs1(node):
    '''노드 끝점으로 부터의 거리를 구하는 dfs'''
    global end
    if len(tree[node])==1 and visit[tree[node][0]] != 0: # end를 통해서 끝점으로부터의 거리를 계산
        end = 0
        return
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            dfs1(n)
            end += 1
            support[node] = max(support[node],end)
            end = support[node]

def dfs2(node):
    '''노드 끝의 D점을 제외하고, 이동해야 하는 거리를 구하는 dfs'''
    global D,start
    for n in tree[node]:
        if visit[n] == 0 and support[n]>=D:
            visit[n] = 1
            start += 1
            dfs2(n)
            start += 1

# 데이터 입력 받아서 트리 구성하기
N,S,D = map(int,input().split())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
support = [0]* (N+1)

start = 0 # 이동 거리
end = 0 # 끝점으로부터의 거리

# 트리 만들기
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# 방문 안해도 되는 노드 찾기
visit[S] = 1
dfs1(S)

# 방문 여부 초기화, 재탐색으로 이동하기
visit = [0] * (N+1)
visit[S] = 1
dfs2(S)

print(start)