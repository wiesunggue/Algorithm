import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr=[int(input())for i in range(N)]
arr.sort()
def chk(l):
    idx=1
    before=0
    cnt=1
    while idx<N:
        if arr[idx]-arr[before]>=l:
            #print(idx,before)
            before=idx
            cnt+=1
        idx+=1
    return cnt
start=0
end=10**20
for i in range(100):
    mid = (start+end)//2
    print('start end',start, mid,end)
    if chk(mid)<M:
        end = mid
    else:
        start=mid+1

print(start-1)