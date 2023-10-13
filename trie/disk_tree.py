# https://www.acmicpc.net/problem/7432
# 디스크 트리

import sys
input = sys.stdin.readline
print = sys.stdout.write
class Node:
    def __init__(self,data):
        self.data=data
        self.child = {}
        self.chk = False
        
class Trie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self,data):
        data = data.split('\\')
        temp = self.root
        for i in data:
            if temp.child.get(i)!=None:
                temp = temp.child[i]
            else:
                new = Node(i)
                temp.child[i]=new
                temp = new
        temp.chk=True
    
def search(node,iter):
    if iter!=0:
        print('-'*(iter-1)+node.data+'\n')
    if node.child=={}:
        return
    for i in sorted(node.child):
        search(node.child[i],iter+1)
        
trie=Trie()
N = int(input())
for i in range(N):
    trie.insert(input().rstrip())

search(trie.root,0)