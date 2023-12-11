# https://www.acmicpc.net/problem/21920
# 백준 21920번 서로소 평균 문제

N = int(input())
arr = list(map(int,input().split()))
X = int(input())

def gcd(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a
ans = 0
cnt = 0
for i in range(N):
    if gcd(arr[i],X) == 1:
        cnt += 1
        ans += arr[i]
        print(ans)

print(f'{ans/cnt:.7f}')