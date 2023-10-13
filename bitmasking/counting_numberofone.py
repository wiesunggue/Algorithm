def bit_count(x):
    if x==0:
        return 0
    return x%2+bit_count(x//2)

def presum(x):
    cnt=0
    for i in range(1,x+1):
        #print(bin(i), bit_count(i))
        cnt+=bit_count(i)
    return cnt

table={0:0}
def recur_presum(x):
    global table
    if table.get(x)!=None:
        return table[x]
    if x<5:
        table[x]=presum(x)
        return table[x]
    # 2의 n승일 경우
    if bit_count(x)==1:
        table[x]=recur_presum(x//2)*2+x//2-1 # 1부터 2**n까지 1의 bit개수는 점화식으로 표현 가능
        # f(2**1) -> 2개
        # f(2**2) -> f(2**1)개*2+2**1-1
        # f(2**3) -> f(2**2)개*2+2**2-1
        # f(2**n) -> f(2**n-1)개*2+2**(n-1)-1
        return table[x]
    for i in range(100):
        if x<(1<<i):
            break
    i-=1 # 켜진 최상위 bit의 위치
    table[x] = recur_presum(1<<i)+recur_presum(x^(1<<i))+x-(1<<i) # 켜진 최상위 비트와 하위 비트로 나눠서 계산 1101을 f(1000)+f(101)으로 바꾸고 101이 의미하는 것은
    # 9, 10, 11, 12, 13에 해당하는 부분으로 x-(1<<i)개의 동일한 최상위 비트 하나씩 저장되는것을 제거하면 5+f(5)와 같으므로 치환하여 계산
    return table[x]

a,b=map(int,input().split())
print(recur_presum(b)-recur_presum(a-1))