arr = [[0 for i in range(100)] for j in range(100)]
N = int(input())
for i in range(N):
    x,y =map(int,input().split())
    for j in range(10):
        for k in range(10):
            arr[x+j][y+k]=1

print(sum(map(sum,arr)))