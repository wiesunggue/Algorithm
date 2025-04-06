import sys
input = sys.stdin.readline

def dfs(node):
    print(node)
    if visited[node]: return False
    visited[node] = 1
    for num in graph[node]:
        if(checked[num]== -1 or dfs(checked[num])):
            checked[num] = node
            return True
    return False

N,M = map(int,input().split())
size = 10
checked = [-1]*size
graph = [[] for i in range(size)]
for i in range(1,N+1):
    graph[i].extend(list(map(int,input().split()))[1:])

ans = 0
for i in range(1,N+1):
    visited = [0] * size
    print('Node', i, checked)
    ans += dfs(i)

print(ans)