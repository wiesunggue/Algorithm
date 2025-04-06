import sys
import random
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class TripNode:
    def __init__(self, key, priority):
        self.left = None
        self.right = None
        self.key = key
        self.priority = priority
        self.size = 1

    def calcSzie(self,root):
        if(root.left): root.size += self.calcSzie(root.left)
        if(root.right): root.size += self.calcSzie(root.right)
        return root.size

class NodePair:
    def __init__(self,left,right):
        self.first = left
        self.second = right


class Trip:
    state = 0
    def __init__(self,root):
        self.root = root

    def split(self,root, key):
        if(root==None): return NodePair(None,None)
        if(root.key < key):
            rs = self.split(root.right, key)
            root.right = rs.first
            return NodePair(root, rs.second)
        else:
            splitted = self.split(root.left, key)
            ls = NodePair(splitted.first,splitted.second)
            root.left = ls.second
            return NodePair(ls.first,root)

    def insert(self, root, node):
        if(root==None): return node
        if(root.priority < node.priority):
            splitted = self.split(root,node.key)
            node.left = splitted.first
            node.right = splitted.second
            return node
        elif (node.key < root.key):
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
        return root

    def merge(self, a, b):
        if(a==None): return b
        if(b==None): return a
        if(a.priority < b.priority):
            b.left = self.merge(a, b.left)
            return b
        else:
            a.right = self.merge(a.right,b)
            return a

    def erase(self, root, key):
        if(root==None): return root
        if(root.key == key):
            ret = self.merge(root.left, root.right)
            self.state = 1
            return ret
        if(key < root.key):
            root.left = self.erase(root.left,key)
        else:
            root.right = self.erase(root.right,key)
        return root

    def search(self,key):
        current_node = self.root
        while current_node:
            print(current_node.key,key,current_node.left,current_node.right)
            if current_node.key == key:
                return 1
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return 0
    def inorder(self,root):
        if (root.left != None): self.inorder(root.left)
        print(root.key,root.priority)
        if (root.right != None): self.inorder(root.right)



N = int(input())
arr = list(map(int,input().split()))
M = int(input())
srr = list(map(int,input().split()))

root = TripNode(arr[0],random.random())
trip = Trip(root)
for i in range(1,N):
    root = trip.insert(root,TripNode(arr[i],random.random()))

ans = []
for i in range(M):
    root = trip.erase(root,srr[i])
    if trip.state == 1:
        root = trip.insert(root,TripNode(srr[i],random.random()))
    ans.append(str(trip.state))
    trip.state = 0
print(ans)
print('\n'.join(ans))