N=int(input())
start,end=-10**18,10**18
mode=0
G=True
H=True
for i in range(N):
    a,b=input().split()
    a=int(a)
    if b=='^':
        start=max(start,a)
        if a==(10**18-1) and end==(10**18):
            end+=1
    elif b=='v':
        end=min(end,a)
        if a==(-10**18+1) and start==(-10**18):
            start-=1
    if (end - start) == 2 and G and H:
        ans = i
        mode = 1
        G=False
    if (end-start)<2 and H:
        ans=i
        mode=2
        G=False
        H=False

if mode==1:
    print('I got it!')
    print(ans+1,end='')
elif mode==2:
    print('Paradox!')
    print(ans+1,end='')
else:
    print('Hmm...',end='')