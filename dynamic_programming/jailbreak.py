# https://algospot.com/judge/problem/read/NUMB3RS
# 알고스팟 문제 두니발 박사의 탈옥

# 문제 : 매일 두니발 박사는 다른 인접한 마을로 이동할 때 D일이 지난 후 각 마을에 있을 확률을 구하라
# N = 마을의 개수, D = 탈옥 후 지난 일 수, P = 교도소의 위치
N,D,P = 5, 2, 0
connected =[[0,1,1,1,0],
      [1,0,0,0,1],
      [1,0,0,0,0],
      [1,0,0,0,0],
      [0,1,0,0,0]]
# 마을 i와 연결된 개수
deg = [0]*N
for i in range(N):
    deg[i] = sum(connected[i])
# 존재할 확률을 계산할 마을의 수
T = 3
# D일 후 0,2,4번 마을의 존재확률을 출력한다
Q = [0, 2, 4]
cache = [[-1]*N for i in range(N)]
def search(path):
    '''모든 가능한 경로를 탐색하고, 가능한 경로에서의 확률을 계산한다'''
    if len(path) == D+1:
        if path[-1] != q:
            return 0.0
        print(path)
        ret = 1.0
        for i in range(len(path)-1):
            ret /= deg[path[i]]
        print('ret',ret)
        return ret
    ret = 0
    for there in range(N):
        if connected[path[-1]][there]:
            path.append(there)
            ret += search(path)
            print(ret)
            path.pop()
    return ret

def search2(here,days):
    '''두니발 박사가 days일째에 here번 마을에 숨어 있을 때, 마지막 날에 q번 마을에 있을 조건부 확률'''
    if days==D:
        return 1 if here==q else 0
    if cache[here][days] > -0.5:
        return ret
    ret = 0.0
    for there in range(N):
        if connected[here][there]:
            ret += search2(there,days+1)/deg[here]
    cache[here][days] = ret
    return ret

q = 0

print(search([P]))

print(search2(P,0))