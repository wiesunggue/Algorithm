import sys
input = sys.stdin.readline

def chk(arr):
    cnt = sum([1 if (i<0.05 or i>0.95) else 0 for i in arr])
    if cnt>360:
        print('A')
    else:
        print('B')
for i in range(100):
    arr = [float(input()) for i in range(5000)]

