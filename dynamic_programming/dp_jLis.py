NEGINF=-10**18

def jlis(indexA, indexB):
    ret = cache[indexA+1][indexB+1]
    if ret!=-1:
        return ret
    ret=2
    a = NEGINF if indexA==-1 else A[indexA]
    b = NEGINF if indexB==-1 else B[indexB]
    maxElement = max(a,b)
    
    for nextA in range(indexA+1,N):
        if maxElement < A[nextA]:
            ret = max(ret, jlis(nextA, indexB)+1)
    for nextB in range(indexB+1,M):
        if maxElement < B[nextB]:
            ret = max(ret,jlis(indexA,nextB)+1)
    cache[indexA+1][indexB+1]=ret
    return ret

N,M=map(int,input().split())
A=list(map(int,input().split()))+[0]*100
B=list(map(int,input().split()))+[0]*100
cache=[[-1 for i in range(101)]for j in range(101)]
print(jlis(-1,-1)-2)
