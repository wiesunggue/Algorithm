# Ax + By = C의 정수해 존재 필요충분조건
# gcd(A, B) | C <=> Ax + By = C의 정수해가 존재한다.

# 기본 문제: 21568 Ax+By=C
# A, B, C가 주어졌을 때 조건을 만족하는 x, y를 찾는 문제
# -1,000,000 < A, B, C <= 1,000,000
# -10억 <= x, y <= 10억
import math


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    next_x = y
    next_y = x - (a // b) * y
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

    if -10**9 <= x <= 10**9 and -10**9 <= y <= 10**9:
        print(x, y)
    else:
        print(-1)

# 로컬 내용에 있던 일반해 정규화 아이디어
# 하나의 해 (x, y)를 구한 뒤 아래와 같이 다른 해로 이동할 수 있다.
# x_step = abs(B // gcd)
# x %= x_step
# y = (C - A * x) // B
# 일반적으로 x = x0 + (B/gcd)t, y = y0 - (A/gcd)t 형태이다.


# 응용 문제: 14565번 역원(Inverse) 구하기
# a + b = 0 (mod n)를 만족하는 b를 구하는 문제
# a * b ≡ 1 (mod n)를 만족하는 b를 구하는 문제
# 1 < a < n, n < 10**12
N, A = map(int, input().split())
plus_inv = N - A
mul_inv = -1

gcd, x, y = extended_gcd(A, N)
if gcd == 1:
    mul_inv = x % N

print(plus_inv, mul_inv)


# 심화 문제: 9267번 A+B
# 연산 1: a = a + b
# 연산 2: b = b + a
# 연산 1, 2를 조합하여 S를 만들 수 있는지 확인하는 문제
# a, b, s < 10**18
A, B, S = map(int, input().split())

# 핵심 질문 1: 연산 1, 2를 조합해서 모든 Ax+By 형태로 만들 수 있는가?
# -> 불가능하다. 예를 들어 5a+5b는 구성할 수 없다.
# 핵심 질문 2: x, y가 양수여야 한다는 제약은 어떻게 처리하는가?
# -> 일반해의 step을 이용해서 양수로 만들어 주어야 한다.
# 이거 개 어려움
