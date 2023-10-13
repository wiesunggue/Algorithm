n,m = map(int,input().split())
tree = [[] for i in range(n)]
for i in range(1,m+1):
    tree[0].append(i)
for i in range(m,n):
    tree[i].append(i+1)

for i in range(n):
    for j in tree[i]:
        print(i,j)
