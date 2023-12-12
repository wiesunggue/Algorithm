def comp2(N,cnt):
    if N%2==0:
        return comp2(N//2,cnt+1)
    return cnt
def comp5(N,cnt):
    if N%5==0:
        return comp5(N//5,cnt+1)
    return cnt
def comp10(N,cnt):
    if N%10==0:
        return comp10(N//10,cnt+1)
    return cnt

def solution():
    T=int(input())
    Diction = {(2**i)*(5**j):(i,j) for i in range(31) for j in range(13)if (2**i)*(5**j)<10**9}
    for test in range(T):
        ans=0
        n,m = map(int,input().split())
        a,b = comp2(n,0),comp5(n,0)
        answer=0
        M=0
        Mv=0
        for key in sorted(Diction):
            x, y = Diction[key]
            if key>m:
                break
            ans=max(ans,min(a+x,b+y))
        if ans==0:
            print(n*m)
            continue
        for key in sorted(Diction):
            x, y = Diction[key]
            if key>m:
                break
            if ans==min(a+x,b+y) and answer==0:
                answer=key*n
                Mv=0
                if x+y==0:
                    M=m
                    break
                tmp=(2**x)*(5**y)
                for i in range(10**9):
                    Mv=tmp*i
                    if Mv>m:
                        break
                M=tmp*(i-1)
                break
        print(n*M)
solution()