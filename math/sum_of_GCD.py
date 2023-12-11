# https://www.acmicpc.net/problem/9613
# 백준 9613번 GCD합

T = int(input())
def gcd(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

def solutions():
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(1,arr[0]+1):
        for j in range(i+1,arr[0]+1):
            ans += gcd(arr[i],arr[j])

    return ans

for test in range(T):
    print(solutions())