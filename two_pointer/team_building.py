# https://www.acmicpc.net/problem/22945
# 백준 22945번 팀 빌딩 문제
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

left,right = 0,1
now = (right-left-1)*min(arr[left],arr[right])
ans = now
# 크기가 커지면 right를 증가시키고, 크기가 줄어들면 left를 증가시킨다.
while left<N and right<N:
    now = (right-left-1)*min(arr[left],arr[right])
    print(left,right,now)
    if ans<=now:
        ans = now
        right+=1
    else:
        left+=1

# right가 마지막에 도달한 경우(N-1)
right-=1
# left가 남아있다면 남은 left를 right까지 이동시킨다
while left!=N:
    now = (right-left-1)*min(arr[left],arr[right])
    print(left,right,now)
    ans = max(ans,now)
    left += 1

print(ans)