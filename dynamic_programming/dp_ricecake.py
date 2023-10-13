arr=[1,1]+[0]*30
for i in range(2,31):
    arr[i]=arr[i-1]+arr[i-2]

a,b=map(int,input().split())
#2가 첫날 7이 둘째날
stop=False
for i in range(1,10000):
    if b-arr[a-3]*i<0:
        break
    if (b-arr[a-3]*i)//arr[a-2]*arr[a-2]==(b-arr[a-3]*i):
        print(f'{i}\n{(b-arr[a-3]*i)//arr[a-2]}')
        break
        
        