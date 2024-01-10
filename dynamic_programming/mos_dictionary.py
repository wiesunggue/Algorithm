# 알고스팟 문제
# https://algospot.com/judge/problem/read/MORSE
# 모스 부호 사전
import sys
sys.setrecursionlimit(10**5)
cache = [[-1] * 205 for i in range(205)]
def combination(n, r):
    if cache[n][r]!=-1: return cache[n][r]
    if r==0 or n==r: return 1
    cache[n][r] = combination(n - 1, r) + combination(n - 1, r - 1)
    return cache[n][r]

def binarysearch(n,m,s):
    ''''''
    global state
    if n==0 or m==0:
        print(s+n*'-'+m*'o')
        return
    left = combination(m+n-1,n-1)
    if state+left<k:
        state+= left
        binarysearch(n,m-1,s+'o')
    else:
        binarysearch(n-1,m,s+'-')

T = int(input())
for test in range(T):
    state = 0
    N,M,k = map(int,input().split())
    binarysearch(N,M,'')