import sys
rinput=sys.stdin.readline
def solution():
    N,M = map(int,rinput().split())
    arr=list(map(int,rinput().split()))
    start,end=1,10**10
    for i in range(100):
        print('*\t',start,end)
        if start>end:
            break
        mid=(start+end)//2
        if using(arr,M,mid):
            end=mid-1
        else:
            start=mid+1
    print(start)
    
def using(arr,M,goal):
    if sum(arr)>M*goal or max(arr)>goal:
        return False
    cnt=1
    s=0
    for i in arr:
        if s+i>goal:
            s=i
            cnt+=1
        else:
            s+=i
    return False if cnt>M else True
if __name__ =='__main__':
    solution()

