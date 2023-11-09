# https://www.acmicpc.net/problem/3584
# 백준 3584번 가장 가까운 공통 조상

# 해결 전략 가능한 부모를 찾고, 해당 값을 저장하는 배열을 선언한다.
# 방문 기록을 하여 방문한 적이 있다면 정지한다. -> 두 번째로 실행하는 부분의 경우 반드시 공통 부모노드를 반환하게 된다.
import sys
sys.setrecursionlimit(10**4+1) # 최대 재귀 = 1만번
input = sys.stdin.readline
def dfs(node):
    global visit, arr
    n = arr[node]
    if n != 0:
        if visit[n] == 0:
            visit[n] = 1
            return dfs(n)
        else: # 한번 방문한 적이 있다면 정지
            return n
    return node # 자기 자신이 공통 부모가 되는 경우
def solution():
    global visit,arr
    N = int(input())
    arr = [0] * (N+1) # 부모 노드는 반드시 1개만 가짐
    visit = [0] * (N+1)

    for i in range(N-1):
        x,y = map(int,input().split())
        arr[y] = x # 부모만 연결하도록 한다.(부모는 1개)
    A,B = map(int,input().split()) # 공통 부모를 구할 노드
    visit[A] = 1
    visit[B] = 1
    dfs(A)
    print(dfs(B))

# 테스트 케이스
T = int(input())
for test in range(T):
    solution()