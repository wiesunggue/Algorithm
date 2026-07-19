import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    next_x = y
    next_y = x - (a//b) * y
    return gcd, next_x, next_y

A, B, C = map(int, input().split())

gcd, x, y = extended_gcd(abs(A), abs(B))
if A < 0:
    x = -x
if B < 0:
    y = -y

if C % gcd != 0:
    print(-1)
else:
    x *= C // gcd
    y *= C // gcd

    if -10**9<=x<=10**9 and -10**9<=y<=10**9:
        print(x, y)
    else:
        print(-1)


# 응용 문제 14565번 역원(Inverse) 구하기
# a + b = 0 (mod n) 를 만족하는 b를 구하는 문제
# a * b ≡ 1 (mod n) 를 만족하는 b를 구하는 문제
# 1<a<n, n<10**12 
import math
N, A = map(int,input().split())
plus_inv = N-A
mul_inv = -1

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    next_x = y
    next_y = x - (a//b) * y
    return gcd, next_x, next_y

gcd, x, y = extended_gcd(A, N)
if gcd == 1:
    mul_inv = x % N

print(plus_inv, mul_inv)

# 심화 문제 : 9267번 A+B 문제
# 연산 1 a = a + b
# 연산 2 b = b + a
# 연산 1, 2를 조합하여 S를 만들 수 있는지 확인하는 문제
# a,b,s< 10**18

A, B, S = map(int,input().split())
# 핵심 질문 1 : 연산 1,2를 조합해서 모든 Ax+By 형태로 만들 수 있는지?? -> 불가능함 ex) 5a+5b를 구성 불가능
# 핵심 질문 2 : x,y는 양수만 가능한데 양수라는 제약을 더할 경우 어떻게 해야 할지? -> step을 이용해서 양수로 만들어 줘야 함
# 이거 개 어려움
