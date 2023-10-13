# https://www.acmicpc.net/problem/24230
# 트리 칠하기

# 재귀를 잘 이용해보자!
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
color = [0]+list(map(int,input().split()))
node = [[]for i in range(N+1)]
visit = [0]*(N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(N):
    node[i].sort()
print(node)
counter=0
def dfs(idx, now_color):
    #print(idx)
    if visit[idx]==1:
        return
    visit[idx]=1
    global counter
    if now_color!=color[idx]:
        counter+=1
        now_color = color[idx]
    
    for i in node[idx]:
        print(idx)
        dfs(i,now_color)


dfs(1,color[1])
print(counter)
