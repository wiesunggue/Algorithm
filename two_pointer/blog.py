# https://www.acmicpc.net/problem/21921
# 백준 21921번 블로그 문제

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(map(int,input().split()))

Nvisit = sum(arr[:K])
count = 1
ans = Nvisit
nextSerial = K
while nextSerial<N:
    Nvisit += arr[nextSerial] - arr[nextSerial - K]
    if ans <= Nvisit:
        count = count*(ans==Nvisit)+1
        ans = max(ans, Nvisit)
    nextSerial +=1

if ans==0:
    print("SAD")
else:
    print(ans)
    print(count)