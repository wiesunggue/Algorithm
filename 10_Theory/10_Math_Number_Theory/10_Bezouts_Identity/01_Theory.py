# Ax + By = C의 x,y 해 존재 필요 충분 조건
# gcd(A,B) | C 가 존재한다 <=> Ax + By = C의 해가 존재한다

# 기본 문제 : 21568 Ax+By=C
# A, B, C가 주어졌을 때 만족하는 x,y를 찾는 문제
# -1000000<A,B,C<=1000000
# -10억 <=x, y <= 10억

import math
def extened_gcd(A, B):
    if B == 0:
        return A, 1, 0
    
    gcd_value, next_x, next_y = extened_gcd(B, A % B)
    x = next_y
    y = next_x - (A//B) * next_y

    return gcd_value, x, y


A, B, C = list(map(int, input().split()))
gcd_value, x, y = extened_gcd(A, B)
print('gcd', gcd_value,x,y)
if C % gcd_value!= 0:
    print(-1)
else:
    if A < 0:
        x = -x
    if B < 0:
        y = -y
    
    scale = C // gcd_value
    x *= scale
    y *= scale

    x_step = abs(B // gcd_value)
    x %= x_step

    y = (C- A*x) // B
    
    if -10**9 <= x <= 10**9 and -10**9 <= y <= 10**9:
        print(x, y)
    else:
        print(-1)


# 응용 문제 : 14565 역원(Inverse)
# 심화 문제 : 9267 A + B
