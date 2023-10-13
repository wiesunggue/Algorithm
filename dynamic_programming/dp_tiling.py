# 종만북 문제
# dynamic programming 비대칭 타일링 문제
# 1권 259p
# 1*2, 2*1의 타일만을 활용하여 만들 수 있는 타일링의 개수를 구하시오
# 단, 타일링은 반드시 비대칭이어야 함

MOD=10**9+7
cache=[-1]*10000
def tiling(width):
    if width<=1:
        return 1
    ret = cache[width]
    if ret!=-1:
        return ret
    ret=tiling(width-2)+tiling(width-1)
    cache[width]=ret
    return ret

def asymmetric(width):
    if width%2==1:
        return (tiling(width)-tiling(width//2)+MOD)%Mod
    ret =tiling(width)
    ret = (ret - tiling(width//2)+MOD)%MOD
    ret = (ret - tiling(width//2-1)+MOD)%MOD
    return ret
