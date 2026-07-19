# 기본 문제 : 1978 소수 찾기
# 02_Prime_Basics에서 진행함

# 응용 문제 : 4134 다음 소수
import math
N = int(input())
arr = [int(input()) for i in range(N)]
result = [-1] * N
for i in range(N):
    if arr[i] <= 2:
        result[i] = 2
        continue
    for next in range(arr[i], 4 * 10**10):
        ans = True
        for k in range(2, math.isqrt(next)+1):
            if next % k == 0:
                ans = False
                break
        if ans == True:
            result[i] = next
            break
    
print(*result, sep='\n')
# 심화 문제 : 15711 환상의 짝궁
import math
MAX_PRIME = 2000000
arr = [True] * (MAX_PRIME+1)
arr[1] = arr[0] = False
for i in range(2, MAX_PRIME+1):
    if arr[i]:            
        power = i * i
        while power <= MAX_PRIME:
            arr[power] = False
            power += i

prime = []
for i in range(MAX_PRIME):
    if arr[i]:
        prime.append(i)

N = int(input())
for i in range(N):
    a,b = map(int, input().split())
    # 홀수 인 경우
    isPrime = True
    if a+b<4:
        isPrime = False
    elif (a+b)%2 == 1:
        check = a+b-2
        for i in range(len(prime)):
            if prime[i] * prime[i] > check:
                break
            if check % prime[i] == 0:
                isPrime = False
                break
    
    print("YES" if isPrime else "NO")
# 골드바흐의 추측
# 강한 골드바흐의 추측 : N>2 이상의 짝수는 두 소수의 합으로 표현할 수 있다(아주 큰 수까지 검증완료)
# 약한 골드바흐의 추측 : N>5는 세 소수의 합으로 표현할 수 있다.(증명됨)
# 기타 : N이 홀수이면 하나의 소수는 반드시 2가 된다.

