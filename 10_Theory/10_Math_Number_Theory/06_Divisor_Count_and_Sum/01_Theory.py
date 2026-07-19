# 약수 개수, 약수의 합

# 기본 문제 : 9506 약수들의 합
# 완전 수 = 약수의 합 = 자기자신
# n이 완전수인지 판단하기
import math
from collections import Counter
SIZE = 100000
SPF = [i for i in range(SIZE+1)]
for i in range(2, math.isqrt(SIZE) + 1):
    if SPF[i] == i:
        p = i * i
        while p <= SIZE:
            if SPF[p] == p:
                SPF[p] = i
            p += i
        
while True:
    n = int(input())
    if n == -1:
        break
    ans = []
    n_copy = n
    while n_copy != 1:
        ans.append(SPF[n_copy])
        n_copy //= SPF[n_copy]
    c = Counter(ans)
    divisors = [1]
    for prime, exp in c.items():
        powers = [prime **i for i in range(exp + 1)]

        new_divisors = []
        for d in divisors:
            for power in powers:
                new_divisors.append(d * power)
        divisors = new_divisors
    divisors.sort()
    divisors.remove(n)
    if sum(divisors) == n:
        print(f'{n} = ' + ' + '.join(map(str, divisors)))
    else:
        print(f'{n} is NOT perfect.')
# 응용 문제 : 17427 약수의 합2 
# 1부터 100만까지 모든 수의 약수를 더한 값을 구하기
N = int(input())
result = N
arr = [0] *(N + 1)
for i in range(2, N + 1):
    result += i
    p = i
    while p <= N:
        arr[p] += i
        p += i
    result += arr[i]
    
# 정 해
# 약수 k의 개수 = N//k 가 된다
N = int(input())
result = 0
for i in range(1,N):
    result += N//i * i
print(result)

# 심화 문제 : 17425 약수의 합
# 1부터 100만까지 약수 합을 10만번 쿼리
import sys
input = sys.stdin.readline

SIZE = 1000000
arr = [0] * (SIZE + 1)
f = [0] * (SIZE + 1)

for i in range(1,SIZE + 1):
    p = i
    while p <= SIZE:
        f[p] += i
        p += i
for i in range(1,SIZE + 1):
    arr[i] = arr[i-1] + f[i]
T = int(input())
query = [int(input()) for i in range(T)]
ans = [0] * T
for i in range(T):
    ans[i] = arr[query[i]]

print('\n'.join(map(str, ans)))
