# https://www.acmicpc.net/problem/3986
# 백준 3986번 좋은 단어
from collections import deque

def checker(s):
    dq = deque(' ')
    for i in range(len(s)):
        if dq[-1]==s[i]:
            dq.pop()
        else:
            dq.append(s[i])
    return len(dq)==1

N = int(input())
ans = 0
for i in range(N):
    s = input()
    ans += checker(s)
print(ans)