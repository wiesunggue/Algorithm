from collections import deque
# 형변환의 문제가 존재함 이를 수정해야함

def addTo(a,b,k):
    bn=len(b)
    an=len(a)
    if an<=bn+k+1:
        a.extend([0]*(bn+k+1))
    for i in range(len(b)):
        a[k+i]+=b[i]
    normalize(a)

def subFrom(a,b):
    for i in range(len(b)):
        a[i]-=b[i]
    normalize(a)
def normalize(num):
    num.extend([0]*11)
    for i in range(len(num)-1):
        if num[i]<0:
            borrow=(abs(num[i])+9)//10
            num[i+1]-=borrow
            num[i]+=borrow*10
        else:
            num[i+1] +=num[i]//10
            num[i]%=10
    while len(num)>1 and num[-1]==0:
        num.pop()
        
def multiply(a,b):
    c=deque([0]*(len(a)+len(b)+1))
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j]+=a[i]*b[j]
    normalize(c)
    return c
def karatsuba(a,b):
    an,bn=len(a),len(b)
    if an<bn:
        return karatsuba(b,a)
    if an==0 or bn==0:
        return ''
    # an이 반드시 긴 자리수
    if an<=50:
        return multiply(a,b)
    half = an//2
    l_a=list(a)
    l_b=list(b)
    a0=deque(l_a[:half])
    a1=deque(l_a[half:])
    b0=deque(l_b[:min(half,len(b))])
    b1=deque(l_b[min(half,len(b)):])
    
    z2=karatsuba(a1,b1)
    z0=karatsuba(a0,b0)
    addTo(a0,a1,0)
    addTo(b0,b1,0)
    z1=karatsuba(a0,b0)
    subFrom(z1,z0)
    subFrom(z1,z2)
    
    ret=[0]
    addTo(ret,z0,0)
    addTo(ret, z1, half)
    addTo(ret, z2, half+half)
    
    return ret

a,b=map(int,input().split())
first = input()
second = input()
first=deque(map(int,reversed(list(first))))
second=deque(map(int,reversed(list(second))))
print(*reversed(karatsuba(first,second)),sep='')