#https://www.acmicpc.net/problem/15988
# 1,2,3더하기
cache=[0,1,2,4]+[0]*1000000
for i in range(4,1000001):
    cache[i]=sum(cache[i-3:i])%1000000009
test=int(input())
for t in range(test):
    N=int(input())
    print(cache[N])