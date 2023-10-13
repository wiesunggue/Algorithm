import heapq
import sys
rinput = sys.stdin.readline

N = int(input())
visit = [0]*N
Node = [[i]+list(map(int,input().split())) for i in range(N)]
print(Node)
def cost(x,y):
    a,b = Node[x],Node[y]
    return min(abs(a[1]-b[1]),abs(a[2]-b[2]),abs(a[3]-b[3]))

def argsort(Node):
    n = len(Node)
    x_dict = {-1:0,n:0}
    y_dict = {-1:0,n:0}
    z_dict = {-1:0,n:0}
    x_reverse = {-1:0,n:0}
    y_reverse = {-1:0,n:0}
    z_reverse = {-1:0,n:0}
    # => 등수를 Node의 index로 바꾸는 부분 x_dict,y_dict,z_dict
    # => Node의 index를 등수로 바꾸는 부분 x_reverse
    for idx,(i,*a) in enumerate(sorted(Node,key=lambda x: x[1])):
        x_dict[idx]=i
        x_reverse[i]=idx
    for idx, (i, *a) in enumerate(sorted(Node,key=lambda x: x[2])):
        y_dict[idx] = i
        y_reverse[i]=idx
    for idx, (i, *a) in enumerate(sorted(Node,key=lambda x: x[3])):
        z_dict[idx] = i
        z_reverse[i] = idx
        
    return x_dict,y_dict,z_dict,x_reverse,y_reverse,z_reverse

print(argsort(Node))

def prim(Node):
    x_dict,y_dict,z_dict,x_reverse,y_reverse,z_reverse = argsort(Node)
    pq = []
    heapq.heappush(pq,(0,0))
    cnt = 0
    x,y,z=0,0,0
    xl,yl,zl = 0,0,0
    while pq:
        cn,idx = heapq.heappop(pq)
        if visit[idx]!=0:
            continue
        visit[idx]=1
        xl,yl,zl = x_dict[x_reverse[idx]-1],y_dict[y_reverse[idx]-1],z_dict[z_reverse[idx]-1]
        xu,yu,zu = x_dict[x_reverse[idx]+1],y_dict[y_reverse[idx]+1],z_dict[z_reverse[idx]+1]
        print(idx,cnt,cn)
        cnt+=cn
        for i in [xl,xu,yl,yu,zl,zu]:
            heapq.heappush(pq,(cost(i,idx),i))
    return cnt

print(prim(Node))

print(visit)
