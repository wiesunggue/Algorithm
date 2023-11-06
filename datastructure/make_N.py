# https://www.acmicpc.net/problem/17255
# 백준 17255번 N으로 만들기

from collections import deque,defaultdict

N = input()
log = defaultdict(int)
def dfs(s):
    # 1가지의 숫자로 이루어진 배열이라면 1반환
    if s[0]*len(s) == s:
        log[s] = 1
        return 1
    # 이미 출현한 적이 있다면 0
    if log[s]!=0:
        return log[s]


    log[s] = dfs(s[1:]) + dfs(s[:-1])
    return log[s]

print(dfs(N))
