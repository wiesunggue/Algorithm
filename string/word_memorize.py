# https://www.acmicpc.net/problem/20920
# 백준 20920번 영단어 암기는 괴로워 문제

import sys
from collections import defaultdict
from functools import cmp_to_key
input = sys.stdin.readline
N,M = map(int,input().split())
word_dictionary = defaultdict(int)
for i in range(N):
    s = input().rstrip()
    if len(s)>=M:
        word_dictionary[s]+=1
def compare(x,y):
    return 1 if (word_dictionary[x],len(x),y)>(word_dictionary[y],len(y),x) else -1

    if word_dictionary[x] > word_dictionary[y]:
        return 1
    elif word_dictionary[x] == word_dictionary[y] and len(x) > len(y):
        return 1
    elif word_dictionary[x] == word_dictionary[y] and len(x) == len(y) and x<y:
        return 1
    return -1

ans = sorted(list(word_dictionary.keys()),key=cmp_to_key(compare),reverse=True)
print('\n'.join(ans))

