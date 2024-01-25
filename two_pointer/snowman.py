# https://www.acmicpc.net/problem/20366
# 백준 20366번 같이 눈사람 만들래?
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
ans = 10**10
for i in range(N):
    for j in range(i+1,N):
        goal = arr[i]-arr[j]
        left, right = j+1,j+2
        while right<N:
            ans = min(ans, abs(goal-arr[left]+arr[right]))
            print(i,j,left,right,ans)
            if arr[left]-arr[right]<=goal:
                right+=1
            else:
                left+=1
                right+= left==right
print(ans)