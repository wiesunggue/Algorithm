# https://www.acmicpc.net/problem/22945
# 백준 22945번 팀 빌딩 문제
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

left,right = 0,N-1
ans = 0
while left<right:
    now = (right-left-1)*min(arr[left],arr[right])
    ans = max(ans,now)
    if arr[left]<arr[right]:
        left+=1
    else:
        right-=1

print(ans)