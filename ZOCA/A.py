N=int(input())
A,Pa,B,Pb=map(int,input().split())
m=0
a,b=0,0
for i in range(10000010):
    tmp=N-Pa*i
    if tmp<0:
        break
    if m<i*A+(tmp//Pb)*B:
        m=i*A+(tmp//Pb)*B
        a,b=i,tmp//Pb
        
print(m)
print(a,b)
