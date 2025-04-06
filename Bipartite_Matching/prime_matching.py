# https://www.acmicpc.net/problem/1017
# 소수 쌍 문제

N = int(input())
arr = list(map(int,input().split()))
first = arr[0]
left = list(filter(lambda x:x%2==0,arr))
right = list(filter(lambda x:x%2==1, arr))
if first==right[0]:
    left,right=right,left

print(left)
left = list(reversed(left))
print(left, right)

isPrime = [0]*2+[1]* 2008

# 에라토스테라스의 체
for i in range(2,2010):
    if isPrime[i]==1:
        x=2
        while x*i<2010:
            isPrime[x*i]=0
            x+=1

link = [[] for i in range(len(left))]
for i,l in enumerate(left):
    for j,r in enumerate(right):
        if isPrime[l+r]:
            link[i].append(j)

print(link)

def dfs(node):
    global visited, ans
    if visited[node]: return False
    visited[node] = 1
    for num in link[node]:
        if(checked[num] == -1 or dfs(checked[num])):
            checked[num] = node
            if left[node]!=first:
                return True
            else:
                visited = [0] * len(left)
                ans.append(right[num])
    print(node, ans)
    return False

checked = [-1]*len(left)
ans = []
for i in range(len(left)):
    visited = [0] * len(left)
    dfs(i)
