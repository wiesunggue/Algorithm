# https://www.acmicpc.net/problem/4134
# 백준 4134번 다음 소수 문제
arr = []
def is_prime(n):
    i=1
    while i*i<=n:
        i += 1
        if n%i == 0 and n!=i:
            return False
    return True
def solutions():
    n = int(input())
    if n<=2:
        return 2
    for k in range(n,5*10**9+1):
        if is_prime(k):
            return k
T = int(input())

for test in range(T):
    print(solutions())

for t in range(100):
    if is_prime(t):
        print(t,is_prime(t))