import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
arr = [{} for i in range(N+1)]
rarr = [{} for i in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    arr[a][b]=i
    rarr[a][b]=i
    rarr[b][a]=i

print(arr)
visit=[0]*(N+1)
ans = ['1']*(N-1)+[N-1]
def dfs(node):
    for idx in rarr[node]:
        if visit[idx]==0:
            if arr[node].get(idx)!=None:
                ans[arr[node].get(idx)]='0'
                ans[-1]-=1
            visit[idx]=1
            dfs(idx)
    
visit[1]=1
dfs(1)
print(ans)
m=100
visit=[0]*(N+1)
print('*'*50)
print(visit)
save=''.join(ans[:-1])
def dfs2(node):
    print(node)
    global m,ans,save
    print('ans',ans)
    if ans[-1]<m:
        save=''.join(ans[:-1])
        m=min(m,ans[-1])
        
    for idx in rarr[node]:
        print('idx',idx)
        if visit[idx]==0:
            temp = arr[node].get(idx)
            print('temp',temp)
            chk = ans[rarr[node][idx]]
            befcount = ans[-1]
            if temp==None:
                ans[rarr[node][idx]]='0'
            else:
                ans[rarr[node][idx]]='1'
            if chk=='1' and ans[rarr[node][idx]]=='0':
                ans[-1]-=1
            if chk=='0' and ans[rarr[node][idx]]=='1':
                ans[-1]+=1
            visit[idx]=1
            dfs2(idx)
            ans[rarr[node][idx]]=chk
            ans[-1]=befcount
visit[1]=1
dfs2(1)
print(save,m)