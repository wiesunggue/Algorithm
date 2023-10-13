# https://www.acmicpc.net/problem/9202
# Boggle 문제
import sys

input = sys.stdin.readline
print = sys.stdout.write

word_len_score = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
pos = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


class Node:
    def __init__(self, data):
        self.data = data
        self.child = {}
        self.total_data = ''


class Trie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self, data):
        temp = self.root
        for i in list(data):
            if temp.child.get(i) != None:
                temp = temp.child[i]
            else:
                new = Node(i)
                temp.child[i] = new
                temp = new
        temp.total_data = data


def backtracking(node, x, y):
    global ans_dict
    if node.total_data != '':
        ans_dict[node.total_data] = 1
    
    for px, py in pos:
        nx, ny = x + px, y + py
        if nx >= 0 and ny >= 0 and nx < 4 and ny < 4 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if node.child.get(arr[nx][ny]) != None:
                backtracking(node.child[arr[nx][ny]], nx, ny)
            visit[nx][ny] = 0


def find_word(ans_dict):
    max_len_word = ''
    max_length = 0
    for i in sorted(ans_dict):
        if max_len_word < i and max_length < len(i) and i != 'score':
            max_len_word = i
            max_length = len(i)
    return max_len_word
def get_score(ans_dict):
    cnt=0
    for i in ans_dict:
        cnt+=word_len_score[len(i)]
    return cnt

trie = Trie()
N = int(input())

for i in range(N):
    trie.insert(input().rstrip())
input()
M = int(input())
visit = [[0 for _ in range(4)] for _ in range(4)]
for k in range(M):
    ans_dict = {}
    arr = [input().rstrip() for _ in range(4 if k == (M - 1) else 5)]
    for i in range(4):
        for j in range(4):
            if trie.root.child.get(arr[i][j]) != None:
                backtracking(trie.root, i, j)
    
    print(f"{get_score(ans_dict)} {find_word(ans_dict)} {len(ans_dict) - 1}\n")