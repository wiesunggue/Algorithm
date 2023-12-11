# https://www.acmicpc.net/problem/22943
# 백준 22943번 수 문제
from collections import Counter
import time
#K,M = map(int,input().split())
K = 5
M = 10**9
optim = 10**(K-1)
arr = [0,0]+[1]*(optim*10+5)
s = set()
ans1 = {}
def prime_search(K,M):
    '''에라토스테네스의 체'''
    for i in range(2,10**K+6):
        if arr[i] != 0:
            s.add(i)
            for j in range(2,10**K+6):
                if i*j>10**K+6:
                    break
                arr[i*j] = 0


def chk2(t):
    if max(Counter(str(t)).values()) != 1:
        return False
    while t%M == 0:
        t = t//M
    for i in range(len(s)):
        if arr[s[i]] == 0:
            return False
        if t%s[i] == 0 and arr[t//s[i]]==1:
            return True
    return False

prime_search(K,M)

st = time.time()
s = sorted(s)
cnt = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        cnt += 1
        if optim<=s[i]+s[j]<optim*10:
            ans1[s[i]+s[j]] = 1


t = 0
for i in ans1:
    t += chk2(i)

et = time.time()
print('조건 탐색',et-st,'cnt',cnt)
print(t)

