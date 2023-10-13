
import sys
import array
rinput = sys.stdin.readline
rprint = sys.stdout.write
global Node,visit,student
cnt=100000
def solve():
    global Node,visit,student,cnt
    N,size = map(int,rinput().split())
    cnt = N
    visit = array.array('b',[0]*(N+1))
    student = array.array('i',[0]*(N+1))
    ans = array.array('i',[0]*(N+1))
    Node = [[] for i in range(N+1)]
    for i in range(size):
        a,b = map(int,rinput().split())
        Node[a].append(b)
    for i in range(1,N+1):
        if visit[i]==0:
            dfs(i)
    for idx,i in enumerate(student):
        ans[i]=idx
    print(*ans[1:])
def dfs(node):
    global cnt
    chk=False
    for i in Node[node]:
        if visit[i]==0:
            chk=True
            visit[i]+=1
            dfs(i)
    if student[node]==0:
        student[node]=cnt
        cnt-=1

if __name__ =="__main__":
    solve()