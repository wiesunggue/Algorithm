def getdiv(n):
    divisorsList = []
    
    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)
    
    divisorsList.sort()
    
    return divisorsList[:-1]

T=int(input())
for test in range(T):
    a=int(input())
    a_list=getdiv(a)
    if sum(a_list)<=a:
        print("BOJ 2022")
        continue
    stop=0
    for i in a_list:
        if sum(getdiv(i))>i:
            print("BOJ 2022")
            stop=1
            break
    if stop==0:
        print("Good Bye")