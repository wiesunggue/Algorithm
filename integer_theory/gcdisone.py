# https://www.acmicpc.net/problem/11689
# GCD(n,k)=1 문제
# gcd(n,k) 인 모든 1<=k<=n의 개수 구하기

N = int(input())
# 빠른 소인수분해
# idx*idx보다 작은 값에 대해서 나눗셈을 하고
# 만약 남은 수가 있다면 idx*idx보다 큰 소수 1개가 들어있는 것임을 활용
def factor(N):
    arr=[]
    idx=2
    while idx*idx<=N+1 and N!=1:
        if N%idx==0:
            cnt=0
            while N%idx==0:
                N=N//idx
                cnt+=1
            arr.append((idx,cnt))
        idx+=1
    if N!=1:
        arr.append((N,1))
    return arr

# 오일러 파이 함수 공식 소수 p에 대해서 pi(p) = p^(k-1)*(p-1)
# pi(a)*pi(b) = pi(ab) if gcd(a,b)==1
def get(p,k):
    # 소수 입력에 대해서 계산하기
    if p==1:
        return 1
    return p**(k-1)*(p-1)
ans=1
# 소수로 이루어진 배열 arr
arr=factor(N)
for a,b in arr:
    # 서로소인 여러 입력값들에 대해서 계산하기
    ans*=get(a,b)
print(ans)