# 약수 함수와 소수 지수
# 기본 문제 : 1676 팩토리얼 0의 개수

N = int(input())
print(N//5+N//25+N//125)


# 응용 문제 : 2004 조합 0의 개수
def count_factor(factor, number):
    ans = 0
    while number:
        ans += number//factor
        number //= factor
    
    return ans

N, M = map(int, input().split())
count2 = count_factor(2, N) - count_factor(2, M) - count_factor(2, N-M)
count5 = count_factor(5, N) - count_factor(5, M) - count_factor(5, N-M)

print(min(count2, count5))


# 심화 문제 : 2904 수학은 너무 쉬워
# 모두 곱해서 나눠버리면 되지 않을까?
import math
from collections import defaultdict
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

d = defaultdict(int)

for i in range(N):
    n = arr[i]
    for j in range(2, math.isqrt(n)+1):
        while n % j == 0:
            n //= j
            d[j] += 1
    if n != 1:
        d[n] += 1

print(d)
ans = 1
for key in d:
    if d[key] >= N:
        ans *= key ** (d[key]//N)

print(ans)