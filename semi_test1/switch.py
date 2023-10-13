from collections import Counter
N = int(input())

A = int('1'+input().replace(' ',''),2)
print(bin(A))
def man(n : int, N : int) -> None:
    global A
    for i in range(1,110):
        if (i*n)>N:
            break
        print('man',N-i*n)
        A = A^(1<<(N-i*n))

def woman(n : int, N : int ) -> None:
    global A
    for i in range(110):
        if (n-i)<=0:
            break
        if (n+i)>N:
            break
        a,b = Counter(bin(A&(1<<(N-(n-i))))),Counter(bin(A&(1<<(N-(n+i)))))
        if a['1']!=b['1']:
            break
        print('****')
        print('pos',N-(n-i))
        print(bin(A))
        A = A ^ ((1<<(N-(n-i))) | (1<<(N-(n+i))))
        print(bin(A))
t = int(input())
for i in range(t):
    a,n = map(int,input().split())
    if a==1:
        man(n,N)
    else:
        woman(n,N)

cnt=0
s=(bin(A)[3:])
for i in s:
    cnt+=1
    if (cnt)%20!=1:
        print(' ',end='')
    if cnt%20==1 and cnt!=1:
        print()

    print(i,end='')