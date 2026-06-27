# 기본 문제 : 1978 소수 찾기
import math
N = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(N):
    if arr[i] == 1:
        continue
    chk = 1
    for j in range(2, math.isqrt(arr[i])+1):
        if arr[i] % j == 0:
            chk = 0
            break
    ans += chk
print(ans)

# 응용 문제 : 2581 소수
M = int(input())
N = int(input())
arr = []
for i in range(M, N + 1):
    if i == 1:
        continue
    chk = True
    for j in range(2, math.isqrt(i)+1):
        if i % j == 0:
            chk = False
            break
    
    if chk:
        arr.append(i)

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])

# 심화 문제 : 1456 거의 소수
# n승인 수를 거의 소수라고 정의
# 1~10^7 까지 소수 찾아서 while문 돌리기
N,M = map(int, input().split())
size = math.isqrt(M) + 1
arr = [True] * (size+1)
arr[0] = False
arr[1] = False

for value in range(2, math.isqrt(size)+1):
    if arr[value] == False:
        continue
    power = value * value
    while power <= size:
        arr[power] = False
        power += value


ans = 0
for prime in range(2, size):
    if arr[prime] == False:
        continue

    power = prime ** 2
    while power <= M:
        if N <= power <= M:
            ans += 1
        power *= prime

print(ans)