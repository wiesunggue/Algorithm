# https://www.acmicpc.net/problem/4315
# 백준 4315번 나무위의 트리 문제

from array import array # 속도 향상을 위해서 list보다는 array를 쓰자!
import sys
sys.setrecursionlimit(10**4+10)
input = sys.stdin.readline
def dfs(node):
    dif_coin,move = beads[node]-1,0
    for n in tree[node]:
        if visit[n] == 0:
            visit[n] = 1
            d,m = dfs(n)
            move += m
            dif_coin += d
    move += abs(dif_coin)
    return dif_coin,move
while True:
    N = int(input())
    if N == 0:
        break
    tree = [[] for i in range(N + 1)]
    visit = [0] * (N+1)
    beads = [0] * (N + 1)
    for i in range(N):
        arr = list(map(int, input().split()))
        parent, bead, child_num = arr[0:3]
        beads[parent] = bead
        for i in range(child_num):
            tree[parent].append(arr[i + 3])
            tree[arr[i+3]].append(parent)
    visit[1] = 1
    print(dfs(1)[1])