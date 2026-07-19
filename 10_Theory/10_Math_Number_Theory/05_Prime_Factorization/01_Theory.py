# 소인수 분해 
# 기본 문제 : 11653 소인수분해
# N<=10000000 이 주어졌을 때 소인수 분해하는 프로그램 만들기
import math
N = int(input())
ans = []
for i in range(2,math.isqrt(N)+1):
    while N % i == 0:
        ans.append(i)
        N //= i
if N != 1:
    ans.append(N)
print(*ans, sep='\n')

# 응용 문제 : 2312 수 복원하기
import math
from collections import Counter
T = int(input())
for i in range(T):
    N = int(input())
    ans = []
    for i in range(2,math.isqrt(N)+1):
        while N % i == 0:
            ans.append(i)
            N //= i
    if N != 1:
        ans.append(N)
    c = Counter(ans)
    for key in sorted(c):
        print(key, c[key])

# 심화 문제 : 16563 어려운 소인수분해
# 1~500만 사이의 수 100만개 소인수 분해하고 그 결과 출력하기
# 최소 소인수 배열 SPF 만들기
# SPF의 Chain을 통해 소인수 분해를 한다.

import math
MAX_SIZE = 5000000
SPF = [i for i in range(MAX_SIZE+1)]

for i in range(2, math.isqrt(MAX_SIZE)+1):
    if SPF[i] == i:
        power = i * i
        while power <= MAX_SIZE:
            if SPF[power] == power:
                SPF[power] = i
            power += i

N = int(input())
arr = list(map(int,input().split()))

result = []
for i in range(N):
    ans = []
    while arr[i] != 1:
        ans.append(SPF[arr[i]])
        arr[i] //= SPF[arr[i]]
    result.append(' '.join(map(str,ans)))
print(*result,sep='\n')