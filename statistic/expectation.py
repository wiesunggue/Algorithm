from math import log2
arr=[0]*40
def bit_count(n):
    if n<=0:
        return
    k=int(log2(n+1))-1 # n보다 작으면서 가장 큰 2의 n승
    for i in range(k+1):
        arr[i]+=2**k
    arr[k+1]+=n-2**(k+1)+1
    bit_count(n-2**(k+1))
#print(bit_count(20))

def exp(n):
    bit_count(n-1)
    ans=0
    for i in range(int(log2(n+1))+1):
        ans+=arr[i]*(n-arr[i])*2**(i)
        print('i',arr[i],n-arr[i],2**(i))
    print(arr)
    print(f'{2*ans/n**2:.2f}')
T = int(input())
for test in range(T):
    arr = [0] * 40
    exp(int(input()))
