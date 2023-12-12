# https://www.acmicpc.net/problem/20300
# 백준 20300번 서강근육맨 문제

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = 0
if N%2==1:
    for i in range(N-1):
        m=max(m,arr[i]+arr[-i-2])
    m=max(m,arr[-1])
else:
    for i in range(N//2):
        m=max(m,arr[i]+arr[-i-1])
print(m)