# https://www.acmicpc.net/problem/3584

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def solve():
    N = int(input())
    tree = [-1]*(N+1)
    for i in range(N-1):
        a,b = map(int,input().split())
        tree[b]=a
    root = tree.index(-1,1)
    def getLevel(node):
        if tree[node]!=-1:
            return getLevel(tree[node])+1
        return 0

    n1,n2 = map(int,input().split())
    L1,L2 = getLevel(n1),getLevel(n2)
    if L1>L2:
        n1,n2=n2,n1
        L1,L2=L2,L1

    for i in range(L2-L1):
        n2 = tree[n2]
    while n1!=n2:
        n1,n2 = tree[n1],tree[n2]
    print(n1)

T = int(input())
for i in range(T):
    solve()