# https://www.acmicpc.net/problem/21276
# 백준 21276번 계보
from collections import defaultdict,deque
# 위상 정렬 문제
N = int(input())
relation = defaultdict(list)
table = {}
visit = {}
arr = input().split()
for name in arr:
    table[name] = 0

M = int(input())
for i in range(M):
    a,b = input().split()
    table[a] += 1
    relation[b].append(a)
que = deque(['root'])
tree = defaultdict(list)
while que:
    name = que.popleft()
    for n in relation[name]:
        table[n] -= 1

    for key in table:
        if table[key] == 0 and visit.get(key) == None:
            visit[key] = 1
            que.append(key)
            tree[name].append(key)


print(len(tree['root']))
print(*sorted(tree['root']))
for key in sorted(table.keys()):
    print(key, len(tree[key]),*sorted(tree[key]))