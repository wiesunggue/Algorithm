# https://www.acmicpc.net/problem/4256
# 백준 4256번 백준 트리 문제

import sys
input = sys.stdin.readline
#print = sys.stdout.write

def solutions():
    def postorder(idx):
        if tree[idx][0] != -1:
            postorder(tree[idx][0])
        if tree[idx][1] != -1:
            postorder(tree[idx][1])
        ans.append(str(idx))

    N = int(input())
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    tree = [[-1,-1] for i in range(N+1)]
    visit = [0]*(N+1)
    root = preorder[0]
    visit[root] = 1

    preidx = 0
    inidx = 0
    ans = []
    while preidx<N and inidx<N:
        while preidx<N and inorder[inidx]!= preorder[preidx]:
            preidx+=1
            visit[preorder[preidx]] = 1
            tree[preorder[preidx-1]][0] = preorder[preidx]

        while inidx<N and visit[inorder[inidx]]:
            inidx+=1
        preidx +=1
        if preidx!=N and inidx!=N:
            visit[preorder[preidx]] = 1
            tree[inorder[inidx-1]][1] = preorder[preidx]
    postorder(root)
    print(' '.join(ans))
T = int(input())
for test in range(T):
    solutions()

