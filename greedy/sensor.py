# https://www.acmicpc.net/problem/2212
# 센서
N=int(input())
K=int(input())
arr=list(map(int,input().split()))
arr.sort()
diff=[0]*(N-1)
for i in range(1,N):
    diff[i-1]=arr[i]-arr[i-1]
diff.sort()
print(diff[:N-K])