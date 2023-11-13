# https://www.acmicpc.net/problem/19641
# 백준 19641번 중첩 집합 모델

# 해당 문제는 트리가 가지는 구간을 계산하는 문제
# dfs의 탐색 순서를 떠올리면 탐색을 시작할 때와 끝날 때 각각 left와 right에 값을 할당하면 된다.
import sys
input = sys.stdin.readline
print = sys.stdout.write
sys.setrecursionlimit(10**5+10)
def dfs(node):
    '''dfs 연산을 통해서 left, right 값 결정 함수'''
    result[node][0] = lr_list[0]
    lr_list[0] += 1
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            dfs(n)
    result[node][1] = lr_list[0]
    lr_list[0] += 1

N = int(input())

# 트리 입력받기
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
result = [[0,0] for i in range(N+1)]
lr_list = [1]
for i in range(N):
    arr = list(map(int,input().split()))[:-1]
    for k in sorted(arr[1:]):
        tree[arr[0]].append(k)
Root = int(input())

# Root노드에서 시작해서 탐색 시작
visit[Root] = 1
dfs(Root)

# 결과 출력하기
for i in range(1,N+1):
    print(f'{i} {result[i][0]} {result[i][1]}\n')

