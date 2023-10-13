import sys
from math import sqrt
from collections import deque
rinput = sys.stdin.readline
rprint = sys.stdout.write

def find(n):
    if disjoint[n] == n:
        return n
    disjoint[n] = find(disjoint[n])
    return disjoint[n]

def cost(x,y):
    return min(abs(x[0]-y[0]),abs(x[1]-y[1]),abs(x[2]-y[2]))

def kruskal(Node):
    x_sort = sorted(Node, key=lambda x: x[0])
    y_sort = sorted(Node, key=lambda x: x[1])
    z_sort = sorted(Node, key=lambda x: x[1])
    cnt = 0
    sv=0
    for a, b, c in Node:
        n_a, n_b = find(a), find(b)
        
        if n_a == n_b:
            continue
        if n_a > n_b:
            disjoint[n_a] = n_b
        else:
            disjoint[n_b] = n_a
        print(a,b,c)
        cnt += c
        sv=c
    return cnt-sv

N = int(input())
disjoint = [i for i in range(N+1)]
Node = [list(map(int,input().split())) for i in range(M)]
print(kruskal(Node))