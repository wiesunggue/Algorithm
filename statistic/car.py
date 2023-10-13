N = int(input())
arr = list(map(int,input().split()))
psum = [0]+[arr[0]]*N
psum_sq = [0]+[arr[0]**2]*N
for i in range(1,N):
    psum[i+1]=arr[i]+psum[i]
    psum_sq[i+1]=arr[i]**2+psum_sq[i]
print(psum)
print(psum_sq)
def get_idx(k):
    chk=0
    idx=1
    for i in range(1,N-k+2):
        m=psum[i+k-1]-psum[i-1]
        m2=psum_sq[i+k-1]-psum_sq[i-1]
        print(m,m2,m2-m**2/k)
        if chk<m2*k-m**2:
            chk=m2*k-m**2
            idx=i
    return idx
for i in range(1,N+1):
    print('***',i,get_idx(i))