# https://www.acmicpc.net/problem/1949
# 백준 1949번 우수마을 문제
import sys
sys.setrecursionlimit(10*4+1)
input = sys.stdin.readline
# 트리에서의 다이나믹프로그래밍
# 문제 해결 전략
# 마을에서 우수마을 On과 Off를 모두 저장한다
# 트리에서의 문제로 바꾸어서 보고
# 만약 해당 마을이 우수마을이 된다면 인접마을은 우수마을이 아니어야 하므로 now_on = sum(before_off)+people[node]가 된다.(now가 on이면 before은 반드시 off가 되어야 한다.)
# 만약 해당 마을이 우수마을이 아니라면 now_off = sum(max(before_on,before_off))가 되어야 한다.(now가 off면 before은 on이어도 되고, off여도 된다.)

N = int(input())
tree = [[] for i in range(N+1)]
visit = [0] * (N+1)
people = [0] + list(map(int,input().split()))
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

#
def find_best_village(node):
    '''node가 우수마을일 때와 우수마을이 아닐 때의 최대 마을사람을 반환하는 함수'''
    now_on,now_off = 0,0
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            before_on,before_off = find_best_village(n)
            now_on += before_off
            now_off += max(before_on,before_off)
    now_on += people[node]
    return now_on,now_off

# 모든 마을이 연결되어 있어서 아무 점에서 시작해도 된다.
visit[1] = 1
print(max(find_best_village(1)))