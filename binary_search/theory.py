# 이진 검색트리 이론
# 이진 검색 트리의 문제점은 균형이 잡히지 않아있다는 문제가 있음
# 균형 잡힌 이진 트리를 구현해야 함
# 일반적으로 '레드-블랙 트리'를 활용해서 구현함
import random
# 알고스팟 너드인가, 너드가 아닌가2 문제
import sys
from sortedcontainers import SortedDict
input = sys.stdin.readline
def isDominated(pos1,pos2):
    return pos1<pos2


# 트립
# K번째 수를 빠르게 검색하기/ K보다 작은 원소의 수 찾기 등

# 이진 검색 트리 간단 구현
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
        print(value)

class BST:
    def __init__(self,root):
        self.root = root

    def insert(self,value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self,value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False
    def delete(self,value):
        is_search = False
        self.parent = self.root
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                is_search = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if is_search == False:
            return False

        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None

            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
        return True


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
            return ret
        if(key < root.key):
            root.left = self.erase(root.left,key)
        else:
            root.right = self.erase(root.right,key)
        return root

    def preorder(self,root):
        print(root.key, root.priority)
        if (root.left != None): self.preorder(root.left)
        if (root.right != None): self.preorder(root.right)

    def inorder(self,root):
        if (root.left != None): self.inorder(root.left)
        print(root.key, root.priority)
        if (root.right != None): self.inorder(root.right)

root = TripNode(0,0)
trip = Trip(root)

N = int(input())
for i in range(N):
    root = trip.insert(root,TripNode(int(input()),random.random()))

print(trip.inorder(root))