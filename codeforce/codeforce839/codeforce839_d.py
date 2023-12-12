def solve(arr):
    start,end=0,10**9
    for i in range(1,len(arr)):
        if arr[i-1]==arr[i]:
            continue
        if arr[i-1]>arr[i]:
            tmp=(arr[i-1]+arr[i]+1)//2
            start=max(start,tmp)
        else:
            tmp=(arr[i-1]+arr[i])//2
            end=min(end,tmp)
    if end<start:
        print(-1)
    else:
        print(start)
    
T=int(input())
for test in range(T):
    input()
    solve(list(map(int,input().split())))
    