from collections import Counter
N = int(input())
for i in range(N):
    a=input()
    b=Counter(a)
    m=0
    for s,i in b.items():
        if i>m and s!=' ':
            m=i
            n=s
    cnt=0
    for s, i in b.items():
        if i == m and s!=' ':
            cnt+=1
    if cnt==1:
        print(n)
    else:
        print('?')