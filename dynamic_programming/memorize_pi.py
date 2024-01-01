# 원주율 외우기 문제(알고스팟)
# https://algospot.com/judge/problem/read/PI

s = '12673939'
N = len(s)
INF = 987654321
def classify(a,b):
    substring = s[a:b]
    if substring == substring[0]*len(substring):
        return 1
    progressive = True
    for i in range(len(substring)-1):
        if ord(substring[i+1])-ord(substring[i]) != ord(substring[1])-ord(substring[0]):
            progressive = False
    if progressive and abs(ord(substring[1])-ord(substring[0]))==1:
        return 2
    alternating = True
    for i in range(len(substring)):
        if substring[i] != substring[i%2]:
            alternating = False
    if alternating: return 4
    if progressive: return 5
    return 10

cache = [-1] * 10020
def memorize(begin):
    if begin == N: return 0
    if cache[begin]!= -1: return cache[begin]
    ret = INF
    for i in range(3,6):
        if begin+i <= N:
            ret = min(ret, memorize(begin+i)+classify(begin,begin+i))
    return ret

print(memorize(0))