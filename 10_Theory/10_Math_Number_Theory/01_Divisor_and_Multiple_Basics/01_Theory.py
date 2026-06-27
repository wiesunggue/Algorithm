import math

# 기본 문제 : 2501 약수 구하기
N, K = map(int,input().split())
arr = []
for i in range(2,N):
    if N%i == 0:
        arr.append(i)

print(arr[K] if len(arr)>=K else 0)
# 응용 문제 : 1037 약수



# 약수는 항상 쌍으로 존재함을 활용하는 문제
N = int(input())
arr = list(map(int,input().split()))

print(min(arr) * max(arr))

# 심화 문제 : 1565 수학
# lcm, gcd에 대해서 chain 처럼 정의가 가능함
# gcd(a,b,c) = gcd(gcd(a,b),c)
D, M = map(int, input().split())
darr = list(map(int,input().split()))
marr = list(map(int,input().split()))

L = 1
for i in range(D):
    L = math.lcm(L, darr[i])

G = 0
for i in range(M):
    G = math.gcd(G, marr[i])

if L % G == 0:
    print(0)
else:
    number = L//G
    ans = 0
    for i in range(1, int(sqrt(number))+1):
        if number % i == 0:
            ans += 1
            ans += i*i != number
    
    print(ans)