import math
A=dict()
N=int(input())
for i in range(N):
    a,b=input().split()
    b=int(b)
    if A.get(a)!=None:
        A[a]+=b
    else:
        A[a]=b
        
ans=sorted(list(A.values()))
booltmp=True
for i in range(len(ans)):
    if booltmp==False:
        break
    for j in range(len(ans)):
        if i==j:
            continue
        if math.floor(ans[i]*1.618)==ans[j]:
            booltmp=False
            break

if booltmp==False:
    print("Delicious!")
else:
    print("Not Delicious...")