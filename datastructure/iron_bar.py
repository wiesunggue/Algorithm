# https://www.acmicpc.net/problem/10799
# 백준 10799 쇠막대기
from collections import deque

s = input()
snx = 0
ans = 0
for i in range(len(s)):
    if s[i]=='(':
        snx += 1
    elif s[i-1]=='(' and s[i]==')':
        snx -= 1
        ans += snx
        print(snx, ans, s[i])
    else:
        ans += 1
        snx -= 1
print(ans)