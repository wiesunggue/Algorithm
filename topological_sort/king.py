# https://www.acmicpc.net/problem/5021
# 왕위 계승
from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
king = input().rstrip()
family_tree={}
family_dict={}
table={}

for i in range(N):
    c,a,b=input().rstrip().split()
    family_dict[a]=0
    family_dict[b]=0
    family_dict[c]=0
    if family_tree.get(a)==None:
        family_tree[a]=[]
        table[a]=0
    family_tree[a].append(c)
    if family_tree.get(b)==None:
        family_tree[b]=[]
        table[b]=0
    family_tree[b].append(c)
    if table.get(c)==None:
        table[c]=2
    if family_tree.get(c)==None:
        family_tree[c]=[]
family_dict[king]=1
table[king]=0

def bfs():
    dq = deque()
    for i in table.keys():
        if table[i]==0:
            dq.append((i,family_dict[i]))
    while dq:
        name,blood = dq.popleft()
        for n in family_tree[name]:
            table[n]-=1
            family_dict[n]+=blood/2
            if table[n]==0:
                dq.append((n,family_dict[n]))
    m=0
    ans=''
    for i in range(M):
        a=input().rstrip()
        try:
            if m<family_dict[a]:
                m=family_dict[a]
                ans=a
        except:
            continue
    print(ans)
bfs()