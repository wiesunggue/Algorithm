# 냅색 이론(재귀 방식)
# 사용 예제
# https://www.acmicpc.net/problem/12865

N, capacity = map(int,input().split())
volumne,need = [],[]
for i in range(N):
    a,b = map(int,input().split())
    volumne.append(a)
    need.append(b)
cache = [[-1]*N for i in range(capacity+1)]

def pack(capacity, item):
    '''재귀 방식으로 knapsack 탐색하고 제한된 가방에 최대한의 가치를 담은 결과를 반환하는 함수'''
    # 기저 사례
    if item==N: return 0
    if cache[capacity][item]!=-1: return cache[capacity][item]

    # 물건을 담지 않는 경우
    ret = pack(capacity, item+1)

    # 이 물건을 담는 경우
    if capacity>=volumne[item]:
        ret = max(ret, pack(capacity-volumne[item],item+1)+need[item])

    cache[capacity][item] = ret
    return ret

def reconstruct(capacity,item,picked):
    '''탐색을 통해서 어떤 물건을 담았는지 탐색하는 함수'''
    if item==N: return
    if pack(capacity, item) == pack(capacity, item+1):
        reconstruct(capacity, item+1, picked)
    else:
        picked.append(item)
        reconstruct(capacity-volumne[item],item+1,picked)

ans = []
reconstruct(capacity,0,ans)
print(ans)