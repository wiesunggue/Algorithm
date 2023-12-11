# https://www.acmicpc.net/problem/5347
# 백준 5347번 LCM 문제
def lcm(a,b):
    if a<b:
        a,b = b,a
    return (a*b)//gcd(a,b)
def gcd(a,b):
    while b!=0:
        r = a%b
        a = b
        b = r
        print(r,a,b)
    return a

for i in range(int(input())):
    a,b = map(int,input().split())
    print(lcm(a,b))