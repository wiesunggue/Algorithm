def gcd(p,q):
    if q==0:
        return p
    return gcd(q,p%q)
N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort()
r_arr=[0]*(N-1)
for i in range(1,N):
    r_arr[i-1]=arr[i]-arr[i-1]

GCD = r_arr[0]
for i in range(1, len(r_arr)):
    GCD = gcd(GCD,r_arr[i])
ans = set()
for i in range(2, int(GCD**0.5)+1):
    if GCD%i==0:
        ans.add(i)
        ans.add(GCD//i)
ans.add(GCD)
print(*sorted(list(ans)))