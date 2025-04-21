# https://www.acmicpc.net/problem/2141
# 백준 2141번 우체국 문제
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for i in range(N)]

arr.sort()

psum = [arr[0][1]]*N
for i in range(1,N):
    psum[i] = psum[i-1]+arr[i][1]

# 0번 위치에서의 거리
ans = 0
for i in range(1,N):
    ans += (arr[i][0]-arr[0][0])*arr[i][1]
nextSerial = 0
for i in range(N-1):
    left_sum = psum[i]
    right_sum = psum[-1]-psum[i]
    dist = arr[i+1][0]-arr[i][0]
    if left_sum*dist-right_sum*dist<0:
        ans += left_sum-right_sum
        nextSerial = i + 1
print(arr[nextSerial][0], ans)