# https://www.acmicpc.net/problem/19581
# 백준 19581번 두 번째 트리의 지름
import sys
sys.setrecursionlimit(10**5+10)
input = sys.stdin.readline
# 문제 해결 전략
# 끝점을 이루는 두 점을 찾고 두 점을 각각 제거했을 때
# 가장 긴 지름을 찾음
def dfs(node):
    '''a'''
    dist = 0
    t = node
    for n,w in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            weight, pos = dfs(n)
            if dist < weight+w:
                dist = weight+w
                t = pos
    return dist,t

N = int(input())
visit = [0] * (N+1)
tree = [[] for i in range(N+1)]

for i in range(N-1):
    a,b,w = map(int,input().split())
    tree[a].append((b,w))
    tree[b].append((a,w))

# 가장 긴 그래프를 이루는 끝점 2개 찾기 end1, end2
start = 1 # 임의의 점에서 시작한다.
visit[start] = 1
end1 = dfs(start)[1] # 최장거리를 이루는 점 1
visit = [0] * (N + 1)
visit[end1] = 1
end2 = dfs(end1)[1] # 최장거리를 이루는 점 2

# end1을 제거하고 탐색하기 -> end1을 제거하고 최장거리 탐색
visit = [0] * (N+1)
start = end2 # 임의의 노드에서 탐색 시작
visit[start] = 1 # start에서 탐색을 시작
visit[end1] = 1 # end1을 제외하고 탐색
ans1 = dfs(end1)[0]

# end2를 제거하고 탐색하기 -> end2를 제거하고 최장거리 탐색
start = end1 # 임의의 노드에서 시작
visit[start] = 1 # start에서 탐색을 시작
visit[end2] = 1 # end2는 노드에서 제거
ans2 = dfs(end2)[0]
#print(end1,end2)
print(max(ans1,ans2)) # 2번째 최장거리는 ans1과 ans2중 큰 값이다
