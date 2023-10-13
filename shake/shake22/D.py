from collections import deque,Counter,OrderedDict
import sys
input = sys.stdin.readline

#N = int(input())
#arr =list(map(int,input().split()))
N=4
arr=[1,3,2,4]
brr= arr.copy()
M = int(input())

dq = deque()
m=arr[0]
dq.append(m)
cnt=0
for i in range(len(arr)):
    if m<arr[i]:
        m=arr[i]
        dq.append(m)
    else:
        cnt+=m-arr[i]
        brr[i]=m

brr=Counter(brr)
crr=sorted((brr).items())
print(crr)
if cnt>M:
    print(0)
else:
    a=0
    c=cnt
    ans=1
    for i in range(len(crr)-1):
        l=crr[i+1][0]-crr[i][0]
        a+=crr[i][1]
        print(l,a)
        c+=a*l
        if c>M:
            break
        ans+=1
    print(ans,c)
    if c<M:
        ans+=(M-c)//N
    print(ans)