# 종만북 문제
# dynamic programming두니발 박사의 탈옥
# 1권 269p
# 그래프에서 하루 한칸씩 움직인다고 할 때, 이동했을 것이라 예상되는 위치의 확률을 출력하는 문제
# 시작점은 감옥 P, 마을의 수 N, 지난 일수 D, T는 확률을 계산할 마을의 수, Q는 마을의 노드
N,D,P=map(int,input().split())
connected=[list(map(int,input().split()))for i in range(N)]
# 마을 i와 연결된 도시의 수
deg=[sum(connected[i]) for i in range(N)]
T=int(input())
Q=list(map(int,input().split()))

def search(path : list):
    if path==d+1:
        if path[-1]!=q:
            return 0.0
        ret=1.0
        for i in range(len(path)-1):
            ret /= deg[path[i]]
        return ret
    ret = 0
    for there in range(N):
        if connected[path[-1]][there]:
            path.append(there)
            ret+=search(path)
            path.pop()
    return ret
cache=[[-1 for _ in range(101)] for _ in range(51)]
# days일 째에 here번 마을에 숨어있다고 가정하고,
# 마지막 날에 q번 마을에 숨어 있을 조건부 확률을 반환한다.
def search2(here, days):
    if days==d:
        return 1 if here==q else 0
    ret = cache[here][days]
    if ret>-0.5:
        return ret
    ret=0.0
    for there in range(N):
        if connected[here][there]:
            ret+=search2(there,days+1)/deg[here]
    return ret

search2(here,)