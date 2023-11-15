# https://www.acmicpc.net/problem/2533
# 백준 2533번 사회망 서비스

import sys
sys.setrecursionlimit(10**7+1)
input = sys.stdin.readline # 빠른 입력

# 데이터를 입력 받아서 트리 만들기
N = int(input())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# 트리의 상태는 On/Off로 정의할 수 있다.
# DP의 접근으로 root가 On/Off일 때의 사회망의 개수로 정의한다.
# 임의의 지점에서 Root Node = (Root On 총 On의 숫자, Root Off의 총 Off 숫자)로 정의하자
# 그러면 가능한 조합은
# 1. Root On + 하위 On/Off 섞인 경우
# 2. Root Off + 하위 On
# 이 2가지만 존재한다.
# SNS = (min(하위 On합, 하위 Off합)+1, 하위 Off 합)으로 정의할 수 있다.

def SNS(node):
    '''On/Off여부에 따라 필요한 사람의 수를 반환하는 DFS 기반 함수'''
    if len(tree[node]) == 1 and visit[tree[node][0]] == 1:
        # 종단 노드인 경우
        return 1,0

    bef_on, bef_off = 0, 0
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            on,off= SNS(n)
            bef_on += on
            bef_off += min(on,off) # 하위 노드 중 On/Off중 작은 것을 선택한다.
    root_on = bef_off +1 # root노드가 켜진 경우
    root_off = bef_on
    print(node,root_on,root_off)
    return root_on,root_off

# 시작점을 어디로 보든 상관없이 트리라고 볼 수 있다. -> 1에서 시작
visit[1] = 1
print(min(SNS(1)))