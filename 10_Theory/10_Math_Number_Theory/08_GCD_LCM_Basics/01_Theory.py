# GCD / LCM 기본 성질
# 기본 문제 : 2609 최대공약수와 최소공배수
N, M = map(int ,input().split())

def gcd(N, M):
    if M == 0:
        return N
    return gcd(M, N % M)

print(gcd(N, M))
print(N*M//gcd(N,M))


# 응용 문제 : 17087 숨바꼭질 6
import math
N, S = map(int, input().split())
arr = list(map(int, input().split()))
# S와 diff를 계산
diff = [0] * N
for i in range(N):
    diff[i] = abs(arr[i], S)

diff.sort()
g = 0
for i in range(N):
    g = math.gcd(g, diff[i])

print(g)

# 심화 문제 : 2436 공약수 
g, l = map(int, input().split())
# 1. g * l 이 N * M과 같다
# 2. N = gx, M = gy라고 할 때 gcd(x,y) = 1
# 3. l = g * x * y => xy = l/g

K = l//g
for x in range(math.isqrt(K)+1,-1,-1):
    if K % x == 0:
        y = K // x
        if math.gcd(x,y) == 1:
            print(x*g,y*g)
            break