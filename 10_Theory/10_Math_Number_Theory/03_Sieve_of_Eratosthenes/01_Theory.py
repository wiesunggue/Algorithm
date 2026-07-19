# 기본 문제 : 백준 2960번 에라토스테네스의 체

N, K = map(int, input().split())
arr = [True] * (N+1)
cnt = 0
ans = 0
for i in range(2, N+1):
    if arr[i]:
        cnt += 1
        if cnt == K:
            ans = i
            
        power = i * i
        while power <= N:
            if not arr[power]:
                power += i            
                continue
            arr[power] = False
            
            cnt += 1
            if cnt == K:
                ans = power
            power += i

print(ans)

# 응용 문제 : 1929 소수 구하기

M, N = map(int, input().split())
arr = [True] * (N+1)
arr[1] = arr[0] = False
for i in range(2, N+1):
    if arr[i]:            
        power = i * i
        while power <= N:
            arr[power] = False
            power += i

for i in range(M, N+1):
    if arr[i]:
        print(i)


# 심화 문제 : 6588 골드바흐의 추측
N = 1000000
arr = [True] * (N+1)
arr[1] = arr[0] = False
for i in range(2, N+1):
    if arr[i]:            
        power = i * i
        while power <= N:
            arr[power] = False
            power += i
prime = []
for i in range(2, N+1):
    if arr[i]:
        prime.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(len(prime)):
        if prime[i] > n//2:
            break
        if arr[n-prime[i]]:
            break
    
    if arr[n-prime[i]]:
        print(f"{n} = {prime[i]} + {n-prime[i]}")
    else:
        print("Goldbach's conjecture is wrong.")
