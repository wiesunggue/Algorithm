N, M = map(int, input().split())
ans = 1
for i in range(1000):
    print(M, N%M)
    if N%M==0:
        break
    else:
        M = N%M
        ans += 1

print(ans)