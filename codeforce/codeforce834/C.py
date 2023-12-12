def counter(l,r,x,a,b,cnt):
    if a==b:
        return 0
    if abs(a-b)>=x:
        return 1
    if (abs(a-l)>=x and abs(b-l)>=x) or (abs(a-r)>=x and abs(b-r)>=x):
        return 2
    if (abs(a-l)>=x and abs(l-r)>=x and abs(b-r)>=x) or (abs(a-r)>=x and abs(r-l)>=x and abs(l-b)>=x):
        return 3
    else:
        return -1
def solution():
    T = int(input())
    for test in range(T):
        l,r,x = map(int,input().split())
        a,b = map(int,input().split())
        print(counter(l,r,x,a,b,0))

solution()