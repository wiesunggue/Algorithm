import sys
input = sys.stdin.readline

class tree:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

def post_dfs(tree): # post order로 출력하는 함수
    if tree is not None:
        post_dfs(tree.left)
        post_dfs(tree.right)
        print(tree.x,end='')

def make_tree(preorder, inorder):
    #print(preorder, inorder)

    if len(inorder)==0: # 기저 사례
        return None

    split_str = inorder.find(preorder[0]) # 조각난 문자열에서 루트노드의 위치
    if split_str==-1: # 기저 사례
        return None

    Tree = tree(preorder[0]) # 루트노드
    left=""
    right=""
    # inorder문자열에서 root노드의 위치를 기준으로 분할하기
    for i in preorder[1:]: # 루트노드 제외
        if i in inorder[:split_str]:
            left+=i
        else:
            right+=i
    #print(preorder[0],"**",left,'**',right)
    Tree.left = make_tree(left, inorder[:split_str]) # 왼쪽노드 추가
    Tree.right = make_tree(right, inorder[split_str+1:]) #오른쪽 노드 추가
    print(preorder[0],end='')
    return Tree

while True:
    try:
        preorder, inorder = map(str, input().rstrip().split())
        make_tree(preorder,inorder)
        print()
    except: # eof error
        break

#post_dfs(make_tree('DBACEGF', 'ABCDEFG'))