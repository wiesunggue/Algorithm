# 기본 문제 : 21568
# 배주 항등식에서 동일 문제 다뤄서 스킵

# 심화 문제 : 14656 
# 배주 항등식에서 동일 문제 다뤄서 스킵

# 응용 문제 : 3955 캔디 분배
# K명이 참가하는 파티에 C개씩 판매하는 캔디를 정확하게 Ky+1개 준비하려고 하는 상황
# 0 < K,C < 10**9

# => Cx === 1 (mod K)
# Cx + Ky = 1의 해 찾기
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    next_x = y
    next_y = x - (a//b) * y
    return gcd, next_x, next_y

T = int(input())
for t in range(T):
    K, C = map(int,input().split())
    gcd, x, y = extended_gcd(C, K)
    if gcd != 1:
        print("IMPOSSIBLE")
    else:
        # x는 양수가 되어야 함
        # C가 1 => x = K+1 이 되면 됨
        # K가 1 => 항상 x = 1이 됨
        x = x % K
        y = (1 - C * x) // K
        if y == 0:
            x += K
            y -= C

        print(x)
        