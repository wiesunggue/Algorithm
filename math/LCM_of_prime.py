# https://www.acmicpc.net/problem/21919
# 백준 21919번 소수 최소 공배수

N = int(input())
arr = list(map(int,input().split()))

def is_prime(p):
    if p==2:
        return True
    i = 1
    while i*i<=p:
        i+=1
        if p%i == 0:
            return False
    return True

ans = set()
for i in range(N):
    if is_prime(arr[i]):
        ans.add(arr[i])
from functools import reduce
if len(ans) == 0:
    print(-1)
else:
    print(reduce(lambda x,y:x*y, ans))
