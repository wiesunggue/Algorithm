# https://www.acmicpc.net/problem/14725
# 개미굴 문제

import sys
import math

input = sys.stdin.readline


class Node:
    def __init__(self,data):
        self.data=data
        self.child={}
        self.chk=False

class Trie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self, data):
        temp = self.root
        for i in data:
            if temp.child.get(i)!=None:
                temp=temp.child[i]
            else:
                new = Node(i)
                temp.child[i]=new
                temp=new
        temp.chk=True
    
def search(node,iter):
    if iter != 0:
        print('--' * (iter - 1) + node.data)
    if node.chk == True:
        return
    for c in sorted(node.child):
        search(node.child[c], iter + 1)

        
trie = Trie()
for _ in range(int(input())):
    information = input().rstrip().split()[1:]
    trie.insert(information)

search(trie.root, 0)