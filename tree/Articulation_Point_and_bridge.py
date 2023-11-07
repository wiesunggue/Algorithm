# https://www.acmicpc.net/problem/14675
# 백준 14675번 단절점과 단절선
# 사이클이 없으므로 단절선은 항상 2개의 트리를 나눌 수 있고
# 연결된 간선이 1개 이하인 경우만 제외하면 항상 단절점이된다.
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
tree = [0]*(N+1)
for i in range(N-1):
    s,e = map(int,input().split())
    tree[s]+=1
    tree[e]+=1
M = int(input())
for i in range(M):
    query, pos = map(int,input().split())
    print('yes\n' if (tree[pos]>=2) or (query >= 2) else 'no\n')