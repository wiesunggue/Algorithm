N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort()
m = 10
start,end=0,0

def find_add(start,end):
    if arr[end]-arr[start]>=5:
        return 1000
    else:
        return 5-(end-start+1)
while start<=end and end<N:
    tmp = find_add(start,end)
    print(tmp)
    m = min(m,tmp)
    if tmp<5:
        end+=1
    else:
        if start==end:
            start+=1
            end+=1
        else:
            start+=1

print(m)