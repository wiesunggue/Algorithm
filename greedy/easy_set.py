for i in range(100):
    a=i
    x=a//5
    y=(a-x*5)//2 if (a-x*5)%2==0 else (a+5-a//5*5)//2-1
    print(i,x,y)
    if a%5==0:
        print(i,a//5)
    else:
        print(i,x+y if a!=1 and a!=3 else -1)
    