# 종만북 문제
# dynamic programming Quantization 문제
# 1권 245p
# 문제 설명 : N개의 수를 s개로 양자화 하였을 때 오차의 제곱합이 최소가 되도록 하는 수를 구하시오
# 1,1,1,2,2,3,3,3 이고 s=3이면 1,2,3으로 양자화하여 최소, s=2이면 1,3으로 양자화하여 0+0+0+1+1+0+0+0=2가 최소
INF = 987654321
n=9
A=[1,744,755,4,897,902,890,6,777]+[0]*(101-n)
pSum=[0]*101
pSqSum=[0]*101
cache=[[-1 for _ in range(101)]for _ in range(101)]

def precalc():
    A[0:n]=sorted(A[0:n])
    pSum[0]=A[0]
    pSqSum[0]=A[0]**2
    for i in range(1,n):
        pSum[i]=pSum[i-1]+A[i]
        pSqSum[i]=pSqSum[i-1]+A[i]**2
    
def minError(lo : int,hi : int) -> int:
    psum=pSum[hi]-(0 if lo==0 else pSum[lo-1])
    sqSum=pSqSum[hi]-(0 if lo==0 else pSqSum[lo-1])
    m=int(0.5+psum/(hi-lo+1))
    ret = sqSum - 2*m*psum + m*m*(hi-lo+1)
    return ret

def quantize(fr : int, parts : int) -> int:
    if fr==n:
        return 0
    if parts==0:
        return INF
    ret=cache[fr][parts]
    if ret!=-1:
        return ret
    ret=INF
    for partSize in range(1,n-fr+1):
        ret = min(ret, minError(fr,fr+partSize-1)+quantize(fr+partSize,parts-1))
    cache[fr][parts]=ret
    return ret
precalc()
print(A)
print(quantize(0,9))