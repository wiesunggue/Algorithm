# 종만북 문제
# dynamic programming 우물을 기어오르는 달팽이 문제
# 1권 256p
# 각 날마다 50% 확률로 1m 또는 2m올라갈 때 m일 안에 n미터를 올라갈 확률을 구하시오
n,m=6,5
MAX_N=100
cache=[[-1 for i in range(MAX_N)]for j in range(2*MAX_N+1)]

def climb(days,climbed):
    if days==m:
        return 1 if climbed>=n else 0
    ret = cache[days][climbed]
    print(days,climbed)
    if ret!=-1:
        return ret
    cache[days][climbed] = climb(days+1,climbed+1)+climb(days+1,climbed+2)
    ret = cache[days][climbed]
    return ret

print(climb(0,0)/2**m)