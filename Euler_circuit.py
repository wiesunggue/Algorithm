import sys
import array
sys.setrecursionlimit(10**7)

rinput = sys.stdin.readline
rprint = sys.stdout.write

global circuit,graph,cnt,visit,adj
cnt=[0]
# dfs로 오일러 경로 탐색
def getEulerCircuit(here, circuit):
    if visit[here]==True: # 방문 가능한 최대횟수만큼 방문했는지 체크
        circuit[cnt[0]] = here + 1
        cnt[0] += 1
        return
    for there in graph[here]:
        while adj[here][there]>0:
            adj[here][there]-=1
            adj[there][here]-=1
            getEulerCircuit(there,circuit)
    visit[here]=True
    circuit[cnt[0]]=here+1
    cnt[0]+=1

def solve():
    global circuit,graph,cnt,visit,adj
    circuit=[0]*10**7 #미리 저장공간 선언
    N = int(input())
    adj = [list(map(int,rinput().split())) for i in range(N)]
    edge = list(map(sum,adj))
    visit = [False]*N
    # 존재하지 않는 노드 체크
    for i in range(N):
        if edge[i]==0:
            visit[i]==True
    edge = sum(edge) # 오일러 경로와 간선의 개수가 일치하는지 확인용
    graph = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if adj[i][j]!=0:
                graph[i].append(j) # 방향을

    # 간선의 개수가 짝수가 아니라면 종료
    if edge%2!=0:
        print(-1)
        return

    getEulerCircuit(0,circuit) # 오일러 경로를 찾는 함수

    ans = circuit[:cnt[0]] # 정답이 차지하는 크기만큼을 따로 추출
    visitchk = [False for i in range(N+1)] # 방문 여부를 확인해서 모든 노드에 방문하였는지 확인
    for i in ans:
        visitchk[i]=True
    # 마지막이 자기 자신이고, 방문 경로의 개수가 일치하고, 모든 노드에 방문하였다면 방문 경로를 출력
    if circuit[0]==circuit[cnt[0]-1] and edge//2+1==cnt[0] and sum(visitchk)==N:
        for i in reversed(ans):
            rprint("{} ".format(i))
    else:
        print(-1)
if __name__ == "__main__":
    solve()