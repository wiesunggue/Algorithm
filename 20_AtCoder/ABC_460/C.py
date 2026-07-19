N, M = map(int, input().split())
shari = list(map(int,input().split()))
neta = list(map(int, input().split()))

shari.sort()
neta.sort()

p1, p2 = 0,0
ans = 0
while p1<N and p2<M:
    print(shari[p1], neta[p2])
    if shari[p1] * 2 >= neta[p2]:
        ans += 1
        p1 += 1
        p2 += 1
    else:
        p1 +=1

print(ans)
