T = int(input())
MAX = 998244353

# concat(x,y) = x+y(Mod M)인 x,y의 Pair 를 찾기
def solve():
    N, M = map(int,input().split())

    ans = 0
    digit = 1
    valid = 0
    while True:
        print((min(N+1,10**digit)-(10**(digit-1))))
        valid += (min(N+1,10**digit)-(10**(digit-1)))
        ans = (ans + N//M * (min(N+1,10**digit)-(10**(digit-1)))) % MAX
        if N < 10 ** digit:
            break
        digit += 1

    print('valid', valid, N, valid==N)
    return ans

for t in range(T):
    print(solve())

def f():
    cnt = 0
    N = 9999
    digit = 4
    M = 1234
    for i in range(1,N+1):
        if ((10**digit * i) % M == i%M):
            cnt += 1
            print(i)

    print(cnt, N//M)

f()