seg=[0]*(N*4)
def build(node,left,right):
    if left==right:
        seg[node]=arr[left]
    
    build(node*2,left,(left+right)//2) #왼쪽 노드
    build(node*2+1,(left+right)//2,right) #오른쪽 노드
    seg[node]=seg[node*2]+seg[node*2+1]

def change(node,left,right,x,y,pos,value):
    if y<left | right<x:
        return
    if left==right:
        seg[left]=value
        return
    change(node*2,left,(left+right)//2,pos,value)
    change(node*2+1,(left+right)//2,right,pos,value)
    seg[node]=seg[node*2]+seg[node*2+1]
    
def load(node,left,right,x,y):
    if y<left | right<x:
        return 0
    if