# 유클리드 호제법
# 기본 문제 : 1934 최소공배수
import math
T = int(input())
for test in range(T):
    n, m = map(int, input().split())
    print(n//math.gcd(n,m)*m)

# 응용 문제 : 2485 가로수
# 가로수의 좌표가 배열로 주어질 때, 모든 가로수의 거리가 동일해지도록 추가해야하는 가로수의 개수
import math
N = int(input())
arr = [int(input()) for i in range(N)]
ans = 0
for i in range(1,N):
    ans = math.gcd(ans,arr[i]-arr[0])

print((arr[-1]-arr[0])//ans + 1 - N)

# 심화 문제 : 14476 최대공약수 하나 빼기
import math
N = int(input())
arr = list(map(int,input().split()))

# prefix gcd, suffix gcd 구하기

L = [0] * (N + 1) # 0부터 i까지 gcd 결과
R = [0] * (N + 1) # i부터 N까지 gcd 결과

for i in range(N):
    L[i] = math.gcd(L[i-1],arr[i])
    R[N - i - 1] = math.gcd(R[N - i],arr[N - i - 1])

ans = 0
value = 0
for i in range(N):
    data = math.gcd(L[i - 1], R[i + 1])
    if arr[i] % data != 0 and ans < data:
        ans = data
        value = arr[i]

if ans != 0:
    print(ans, value)
else:
    print(-1)