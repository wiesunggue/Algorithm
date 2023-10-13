import sys
import math
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.child = {}
        self.check = False

class Trie:
    def __init__(self):
        self.root = Node('')
    def insert(self,information):
        tmp = self.root
        for data in information:
            if tmp.child.get(data)!=None:
                tmp = tmp.child[data]
            else:
                new = Node(data)
                tmp.child[data] = new
                tmp = new
        tmp.check=True

def search(node,iter):
    if iter!=0:
        print('*****','--' * (iter-1) + node.data)
    if node.check==True:
        return
    for c in sorted(node.child):
        search(node.child[c],iter+1)
    
trie = Trie()
for _ in range(int(input())):
    information = input().rstrip().split()[1:]
    trie.insert(information)
 
search(trie.root,0)
