# https://www.acmicpc.net/problem/5397
# 백준 5397번 키로거
from collections import deque
def key_log(s):
    left = deque()
    right = deque()
    for i in range(len(s)):
        if s[i] == '<':
            try:
                right.appendleft(left.pop())
            except:
                pass
        elif s[i] == '>':
            try:
                left.append(right.popleft())
            except:
                pass
        elif s[i] == '-':
            try:
                left.pop()
            except:
                pass
        else:
            left.append(s[i])
    # right에 있는 모든 문자 빼주기
    #while right:
    #    left.append(right.popleft())
    return ''.join(left)

def solutions():
    N = int(input())
    for i in range(N):
        s = input()
        print(key_log(s))

solutions()
