# https://www.acmicpc.net/problem/9202
# Boggle 문제
import time
import sys, random

input = sys.stdin.readline
# print = sys.stdout.write
word_len_score = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11, 9: 11, 10: 11}
pos = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
d = {'a': 0}


class Node:
    def __init__(self, data):
        self.data = data
        self.child = [0] * 26
        self.chk = 0
        self.total_data = ''


class Trie:
    def __init__(self):
        self.root = Node('')
    
    def insert(self, data):
        temp = self.root
        for i in list(data):
            if temp.child[ord(i) - 65] != 0:
                temp = temp.child[ord(i) - 65]
            else:
                new = Node(i)
                temp.child[ord(i) - 65] = new
                temp = new
        temp.chk = word_len_score[len(data)]
        temp.total_data = data


def backtracking(node, x, y):
    global ans_dict
    if ans_dict.get(node.total_data) == None and node.total_data != '':
        ans_dict['score'] += node.chk
        ans_dict[node.total_data] = 1
    
    for px, py in pos:
        nx, ny = x + px, y + py
        if nx >= 0 and ny >= 0 and nx < 4 and ny < 4 and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if node.child[ord(arr[nx][ny]) - 65] != 0:
                backtracking(node.child[ord(arr[nx][ny]) - 65], nx, ny)
            visit[nx][ny] = 0


def find_word(ans_dict):
    max_len_word = ''
    max_length = 0
    for i in sorted(ans_dict):
        if max_len_word < i and max_length < len(i) and i != 'score':
            max_len_word = i
            max_length = len(i)
    return max_len_word


trie = Trie()

start = time.time()
for i in range(300000):
    trie.insert(''.join([chr(random.randint(65, 90)) for i in range(random.randint(5, 8))]))
print(f'실행시간 :{time.time() - start}')
start = time.time()

M = 100
visit = [[0 for _ in range(4)] for _ in range(4)]
for k in range(M):
    ans_dict = {'score': 0}
    arr = [''.join([chr(random.randint(65, 90)) for i in range(4)]) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if trie.root.child[ord(arr[i][j]) - 65] != 0:
                backtracking(trie.root, i, j)
    
    print(f"{ans_dict['score']} {find_word(ans_dict)} {len(ans_dict) - 1}\n")
print(f'실행시간 :{time.time() - start}')